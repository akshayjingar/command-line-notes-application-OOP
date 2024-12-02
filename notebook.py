import datetime

#store the next available id for all new notes
last_id = 0

class Note:
    """
    Represent a note in the notebook. Match against a string in searches and store tags for each note.
    """

    def __init__(self,memo:str,tags='') -> None:
        """
        Initialize a note with memo and option space seperated tags. Automatically set the note's creation date
        and unique id
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id

        last_id += 1
        self.id = last_id
    
    def match(self,filter_):
        """
        Determine if this note matches the filter text. Return True if it matches, False otherwise
        """
        return filter_ in self.memo or filter_ in self.tags


class Notebook:
    """
    Represent a collection of notes that can be tagged, modified & searched
    """

    def __init__(self) -> None:
        """
        Initialize a notebook with an empty list
        """
        self.notes = []

    def new_note(self,memo:str,tags=""):
        """
        Create a new note andadd it to the list
        """
        self.notes.append(Note(memo,tags))


    def _find_note(self,note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
            
        

    def modify_memo(self,note_id,memo):
        """
        Find the note with the given id and changes its memo to the given value
        """
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        else:
            return False
    
    def modify_tags(self,note_id,tags):
        """
        Find the note with the given id and changes its memo to the given value
        """
        self._find_note(note_id).tags = tags
    
    def search(self,filter_):
        """
        Find all notes that match the given filter string
        """
        return [
            note for note in self.notes if note.match(filter_)
        ]

if __name__=='__main__':
    n = Notebook()

    n.new_note('Hello World')
    n.new_note("hello again")

    print(n.notes)

    for i in n.notes:
        print(f"note index {i.id}, Value : {i.memo}")

    print(n.search('Hello'))