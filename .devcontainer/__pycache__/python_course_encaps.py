class Any:
    def __init__(self,) -> None:
        self.public = "this is public"
        self._protected = 'this is protected'
        
        self._metodo_protected()

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'
    
    
a = Any()