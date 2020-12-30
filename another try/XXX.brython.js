__BRYTHON__.use_VFS = true;
var scripts = {"$timestamp": 1607751472885, "test": [".py", "print(\"first\")\nfrom test2 import test_print\ntest_print(\"asdf\")\n", ["test2"]], "test2": [".py", "print(\"second\")\ndef test_print(text):\n print(text)\n", []]}
__BRYTHON__.update_VFS(scripts)
