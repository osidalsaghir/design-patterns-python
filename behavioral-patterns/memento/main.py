class TextDocument:
    def __init__(self):
        self._content = ""

    def set_content(self, content):
        self._content = content

    def get_content(self):
        return self._content

    def create_memento(self):
        return TextDocumentMemento(self._content)

    def restore_from_memento(self, memento):
        self._content = memento.get_saved_content()
        
class TextDocumentMemento:
    def __init__(self, content):
        self._saved_content = content

    def get_saved_content(self):
        return self._saved_content

class HistoryManager:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]

if __name__ == "__main__":
    text_document = TextDocument()
    history_manager = HistoryManager()

    # User types and saves content
    text_document.set_content("Hello, World!")
    history_manager.add_memento(text_document.create_memento())

    print("Current Content:", text_document.get_content())  # Output: "Hello, World!"
    
    # User continues editing
    text_document.set_content("Hello, Osid!")
    history_manager.add_memento(text_document.create_memento())

    print("Current Content:", text_document.get_content())  # Output: "Hello, Osid!"
    
    # User wants to undo to the previous state
    previous_state_memento = history_manager.get_memento(0)
    text_document.restore_from_memento(previous_state_memento)

    print("Current Content:", text_document.get_content())  # Output: "Hello, World!"
