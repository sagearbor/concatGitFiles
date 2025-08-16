import os

def consolidate_repo():
    """
    Consolidates a repository into a single text file from a subdirectory,
    placing the output file in the script's directory.
    """
    # --- Configuration ---
    # Get the absolute path of the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # The root directory to scan is the parent of the script's directory
    root_dir = os.path.abspath(os.path.join(script_dir, '..'))
    
    # The output file will be created inside the script's directory
    output_filename = os.path.join(script_dir, 'output.txt')
    
    # Get the name of the script's directory to ignore it during the scan
    script_folder_name = os.path.basename(script_dir)

    # Directories to ignore
    ignore_dirs = {'.git', '__pycache__', 'node_modules', 'venv', '.vscode', '.idea', script_folder_name}
    
    # File extensions to ignore
    ignore_extensions = {'.pyc', '.pyo', '.pyd', '.so', '.o', '.a', '.dll', '.exe', '.DS_Store'}
    
    # Specific files to ignore (the script itself and its output)
    ignore_files = {os.path.basename(__file__), os.path.basename(output_filename)}

    print(f"Scanning repository at: {root_dir}")
    print(f"Output will be saved to: {output_filename}")
    
    # Track the number of files processed
    file_count = 0

    try:
        with open(output_filename, 'w', encoding='utf-8', errors='ignore') as outfile:
            for dirpath, dirnames, filenames in os.walk(root_dir, topdown=True):
                # Modify dirnames in-place to prune the search, which is efficient
                dirnames[:] = [d for d in dirnames if d not in ignore_dirs]

                for filename in filenames:
                    # Check for ignored files and extensions
                    if filename in ignore_files or os.path.splitext(filename)[1] in ignore_extensions:
                        continue

                    file_path = os.path.join(dirpath, filename)
                    # Make the path in the output file relative to the repo root
                    relative_path = os.path.relpath(file_path, root_dir)

                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                            content = infile.read()
                        
                        # Write the file header and content to the output file
                        # Use forward slashes for cross-platform compatibility in the header
                        outfile.write(f"---\nFile: {relative_path.replace(os.sep, '/')}\n---\n")
                        outfile.write(content)
                        outfile.write("\n\n")
                        
                        file_count += 1
                        print(f"Processed: {relative_path}")

                    except Exception as e:
                        print(f"Could not read file {file_path}: {e}")
                        
    except IOError as e:
        print(f"Error writing to output file {output_filename}: {e}")
        return

    # Removed the emoji from the print statement to prevent UnicodeEncodeError on Windows
    print(f"\nSuccess! Consolidated {file_count} files into '{os.path.basename(output_filename)}'.")

if __name__ == '__main__':
    consolidate_repo()
