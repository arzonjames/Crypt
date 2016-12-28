import hashlib

class Crypt():

    """
       Created by James W, Some rights are reserved.
       
       DISCLAIMER: The full makers of Crypt are not
       liable for any damage or cause, that is used for
       the malicious content of abuse and/or destruct-
       ion. Discrepancy is advised.
       
       Crypt is a new project, an evolved version of a
       dead project, formerly named "Hook". To learn
       more about Crypt, please visit the Arzon website.
       
       http://arzondevelopment.com
    """

    def __init__( self ):
        self.table = []
        self.row = 0
        self.err = 0
        self.session = False
        self.key = "@!Y)(^C&"
    
    def EncryptKey( self, key ):
        k = hashlib.md5( self.key.encode( key ) ).hexdigest()
        return k

    def EncryptTable( self, table ):
        return EncryptKey( table ).digest()[ 0: ]
    
    def StartSession( self ):
                
        if self.session == False:
            try:
                self.session == True
            except:
                print(
                    "Failed to start session.\n" +
                    "(CryptPy module timeout, or session is already active)"
                )
                self.err = self.err + 1

    def EndSession( self ):
                
        if self.session == True:
            try:
                self.session == True
            except:
                 print(
                    "Failed to end session.\n" +
                    "(CryptPy module timeout, or session is already over)"
                 )
                 self.err = self.err + 1
    
    def Create( self, name, args ):

        while self.session == True:
            
            for i in self.table:

                if name in self.table[ i ]:
                    print(
                        "Failed to create a new encryption.\n" +
                        "(Name already exists)"
                    )
                    self.err = self.err + 1
                    break

                elif name:
                    print(
                        "Failed to create a new encryption.\n" +
                        "(No name was entered)"
                    )
                    self.err = self.err + 1
                    break

                else:
                    try:
                        self.row = self.row + 1
                        self.table[ self.row ] = { "name": name, "args": "|".join( args ) }
                    except:
                        print(
                            "Failed to create a new encryption.\n" +
                            "(CryptPy module timeout)"
                        )
                        self.err = self.err + 1
                        break
                        
        else:
            print(
                "Failed to run commands.\n" +
                "(No session)"
            )
            self.err = self.err + 1

    def Remove( self ):

        while self.session == True:
            
            if self.table[ self.row ]:
                print(
                    "Failed to remove an encryption.\n" +
                    "(No name exists)"
                )
                self.err = self.err + 1

            else:
                try:
                    self.table[ self.row ] = {}
                    self.row = self.row - 1
                except:
                    print(
                        "Failed to remove an encryption.\n" +
                        "(CryptPy module timeout)"
                    )
                    self.err = self.err + 1
                    
        else:
            print(
                "Failed to run commands.\n" +
                "(No session)"
            )
            self.err = self.err + 1

    def Argument( self, args ):
        
        while self.session == True:
            
            if self.table[ self.row ]:
                print(
                    "Failed to add an argument to encryption.\n" +
                    "(No name exists)"
                )
                self.err = self.err + 1

            elif self.table[ self.row ][ "args" ]:
                self.table[ self.row ][ "args" ] = "|".join( args )

            else:
                try:
                    self.table[ self.row ][ "args" ] = self.table[ self.row ][ "args" ] + "|" + "|".join( args )
                except:
                    print(
                        "Failed to add an argument to ecnryption.\n" +
                        "(CryptPy module timeout)"
                    )
                    self.err = self.err + 1

        else:
            print(
                "Failed to run commands.\n" +
                "(No session)"
            )
            self.err = self.err + 1
    
    def Errors( self ):
        return self.err
    
    def Row( self ):
        return self.row

    def Table( self, key ):

        if key is EncryptKey( self.key ):
            return self.table

        else:
            print(
                "Failed to get encrypted table data.\n" +
                "(No key or wrong key entered)\n" +
                "--- WARNING ---\n" +
                "Table has been encrypted, please refer"
            )
            self.err = self.err + 1
