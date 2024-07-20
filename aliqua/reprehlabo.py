class Observer:
    def __init__(self):
        self.patches = []

    def record_patch(self, patch):
        self.patches.append(patch)

    def clear_patches(self):
        self.patches = []

# Usage
observer = Observer()
observer.record_patch({'type': 'update', 'key': 'name', 'value': 'Alice'})
observer.record_patch({'type': 'delete', 'key': 'age'})
observer.patches = []  # Equivalent to observer.clear_patches()

print(observer.patches)  # Output: []
