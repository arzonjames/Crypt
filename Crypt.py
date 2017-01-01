class Crypt:
    
    """ A secure virtual database, run by Python. """
    
    # Initiates class module
    def __init__( self, key ):
        self.table = []
        self.row = 0
        self.error = 0
        self.session = False
        self.lock = False
        self.key = key
    
    # Toggles the session
    def Session( self ):
        
        # If session is true
        if self.session == True:
            return self.session = False
            
        # If session is false
        elif self.session == False:
            return self.session = True
            
        else:
            pass
    
    # Creates a new instance
    def Create( self, name, data ):
        row = self.row
        
        # While there is a session
        while self.session == True:
        
            # Sets up check
            for i in self.table:
                
                # If no name given
                if name == "":
                    print(
                        [
                            "No name was given.\n",
                            "(Create error)"
                        ]
                    )
                    self.error += 1
                    
                # If name already exists
                elif name is self.table[i]["name"]:
                    print(
                        [
                            "Name already exists.\n",
                            "(Create error)"
                        ]
                    )
                    self.error += 1
                    
                elif self.lock == True:
                    print(
                        [
                            "Commands are locked.\n",
                            "(Lock is on)"
                        ]
                    )
                    
                # If it checks good
                else:
                    self.row += 1
                    self.table[row] = { "name": name, "args": "|".join( data ) }
                
    # Deletes an instance
    def Delete( self ):
        row = self.row
        
        # While there is a session
        while self.session == True:
        
            # If no instance exists
            if not self.table[row]:
                print(
                    [
                        "No instance exists.\n",
                        "(Remove error)"
                    ]
                )
                self.error += 1
                
            elif self.lock == True:
                print(
                    [
                        "Commands are locked.\n",
                        "(Lock is on)"
                    ]
                )
                
            # If it checks good
            else:
                self.table[row] = ""
                self.row -= 1
            
    # Adds an argument to instance
    def Argument( self, data ):
        row = self.row
        
        # While there is a session
        while self.session == True:
            
            # If current data in instance
            if self.table[row]["args"]:
                ae = self.table[row]["args"]
                self.table[row]["args"] = ae + "|" + "|".join( data )
                
            elif self.lock == True:
                print(
                    [
                        "Commands are locked.\n",
                        "(Lock is on)"
                    ]
                )
            
            # If no data given
            elif not data:
                print(
                    [
                        "No data was given.\n",
                        "(Argument error)"
                    ]
                )
                self.error += 1
                
            else:
                self.table[row]["args"] = "|".join( data )
            
    # Locks and prohibits functions from being run
    def Lock( self ):
    
        # While there is a session
        while self.session == True:
        
            # If unlocked
            if self.lock == False:
                return self.lock = True
                
            else:
                pass
    
    # Unlocks and alows new functions to run
    def Unlock( self ):
        
        # While there is a session
        while self.session == True:
        
            # If locked
            if self.lock == True:
                return self.lock = False
                
            else:
                pass
    
    # Returns current argument in instance
    def cArgs( self ):
        row = self.row
        
        # While there is a session
        while self.session == True:
            
            # If locked
            if self.lock == True:
                print(
                    [
                        "Commands are locked.\n",
                        "(Lock is on)"
                    ]
                )
            
            else:
                return self.table[row]["args"]
        
    # Returns current row
    def cRow( self ):
    
        # While there is a session
        while self.session == True:
            
            # If locked
            if self.lock == True:
                print(
                    [
                        "Commands are locked.\n",
                        "(Lock is on)"
                    ]
                )
            
            else:
                return self.row
        
    # Returns all data in table
    def cTable( self, key ):
        
        # While there is a session
        while self.session == True:
            
            # If correct key
            if key == self.key:
                return self.table
            
            # If locked
            elif self.lock == True:
                print(
                    [
                        "Commands are locked.\n",
                        "(Lock is on)"
                    ]
                )
            
            else:
                print(
                    [
                        "Wrong key!\n",
                        "(TableGet error)"
                    ]
                )
                self.error += 1
            
    # Returns current error count
    def cErr( self ):
        
        # While there is a session
        while self.session == True:
        
            # If locked
            if self.lock == True:
                print(
                    [
                        "Commands are locked.\n",
                        "(Lock is on)"
                    ]
                )
            
            else:
                return self.error