from . import Page, Action


class Doc( Page ):
    def __init__( self ):
        super( Doc, self ).__init__( "Documentation" )

    def init( self ):
        self.add([
            Action.Cmd( "Generate HTML", "cd docs; make html; cd .." ),
            Action.Cmd( "Clean", "cd docs; make clean; cd .." ),
            Action.Back()
        ])