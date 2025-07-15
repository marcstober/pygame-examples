import os
import sys
import traceback
import subprocess

root = os.path.dirname(os.path.abspath(__file__))

failures = []

# Dictionary of script path (relative to root) to list of command line args
script_args = {
    # Example: "recipes/showimage.py": ["--example"],
    "tw.py": ["23:59"],
}


def test_py_files_in_folder(folder):
    for fname in os.listdir(folder):
        fpath = os.path.join(folder, fname)
        relpath = os.path.relpath(fpath, root)
        if fname in {"venv", ".venv"}:
            continue
        if os.path.isdir(fpath):
            # Recurse into subfolders
            test_py_files_in_folder(fpath)
        elif fname.endswith(".py") and fname not in {"smoketest.py", "__init__.py"}:
            args = script_args.get(relpath, [])
            if not len(args):
                print(f"Running {relpath} in {folder}...", end=" ", flush=True)
            else:
                print(
                    f"Running {relpath} in {folder} with args {args}...",
                    end=" ",
                    flush=True,
                )
            try:
                result = subprocess.run(
                    [sys.executable, fname] + args,
                    cwd=folder,
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                if result.returncode == 0:
                    print("OK")
                else:
                    print("FAIL")
                    failures.append((relpath, result.stderr or result.stdout))
            except Exception as e:
                print("FAIL")
                failures.append((relpath, traceback.format_exc()))


if __name__ == "__main__":
    test_py_files_in_folder(root)
    if failures:
        print("\nSome files failed to run:")
        for relpath, err in failures:
            print(f"{relpath}:\n{err}")
        sys.exit(1)
    else:
        print("\nAll scripts ran successfully.")
