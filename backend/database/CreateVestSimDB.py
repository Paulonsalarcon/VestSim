from VestSimDB import VestSimDB

if __name__ == "__main__":
    VestSimDB = VestSimDB()
    VestSimDB.Connect()
    VestSimDB.Create()
    VestSimDB.Migrate()

    
