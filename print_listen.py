with open('scrubhub_tactical_pitch.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'document\.addEventListener\(\'keydown\'(.*?)}\);', text, re.DOTALL)
if match:
    # Print the event listener code
    print("Match found:")
    print(match.group(0))
else:
    print("No match")
