# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import re
import os

class DeadCodeDetector:
    # Heuristic: Find code after 'return', 'throw', 'break', 'continue' in the same block.
    # This is a very naive implementation for Python/JS.
    # It detects:
    # return ...
    # some_code() <--- Dead
    
    # We look for lines containing return/throw/break/continue followed by non-empty lines 
    # at the same indentation level or valid code.
    
    # Actually, a simpler regex approach for "unreachable lines" is tricky without AST.
    # Let's try finding `return` then checking if the next line is indented same or more
    # and is not a comment/decorator/else/elif.
    
    RETURN_PATTERN = re.compile(r'^\s*(return|raise|throw|break|continue)\b')
    
    @staticmethod
    def scan_file(filepath):
        issues = []
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            
            for i, line in enumerate(lines):
                # if line is a return statement
                match = DeadCodeDetector.RETURN_PATTERN.match(line)
                if match:
                    indent = len(line) - len(line.lstrip())
                    
                    # Check subsequent lines
                    for j in range(i + 1, len(lines)):
                        next_line = lines[j]
                        stripped = next_line.strip()
                        
                        if not stripped or stripped.startswith('#') or stripped.startswith('//'):
                            continue
                        
                        next_indent = len(next_line) - len(next_line.lstrip())
                        
                        # If indentation is less, we exited the block (safe)
                        if next_indent < indent:
                            break
                        
                        # If indentation is same, and not 'else'/'elif'/'case'/'default')
                        if next_indent == indent:
                            if stripped.startswith(('else', 'elif', 'case', 'default', 'except', 'catch', 'finally', ')', '}')):
                                break # Control flow change
                            
                            # Otherwise, it's likely dead code
                            issues.append({
                                'line': j + 1,
                                'file': filepath,
                                'content': stripped,
                                'msg': f"Unreachable code detected after '{match.group(1)}'"
                            })
                            break # Only flag the first unreachable line
                        
                        # If indent is greater (nested), it's definitely dead if it follows a return
                        # UNLESS it's inside a function def inside the return? No.
                        # Naive check: yes, dead.
                            
        except Exception:
            pass
        return issues

    @staticmethod
    def scan_directory(directory):
        all_issues = []
        for root, dirs, files in os.walk(directory):
            if 'node_modules' in dirs: dirs.remove('node_modules')
            if '.git' in dirs: dirs.remove('.git')
            
            for file in files:
                if file.endswith(('.py', '.js', '.ts', '.java')):
                    path = os.path.join(root, file)
                    issues = DeadCodeDetector.scan_file(path)
                    all_issues.extend(issues)
        return all_issues

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
