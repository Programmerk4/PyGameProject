from appJar import gui
import sqlite3

# Connect to database
connection = sqlite3.connect("login.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS User (Username varchar(20) PRIMARY KEY, Password varchar(20))")
connection.commit()
cursor.execute("SELECT * From User")
print(cursor.fetchall())


# Check button input
def press(name):
    # When cancel is pressed
    if name == "cancel":
        win.stop()
    # When register is pressed
    elif name == "register":
        if len(win.getEntry("username")) < 20 and len(win.getEntry("password")) < 20:
            query = "SELECT COUNT(*) FROM User WHERE Username == \"%s\"" % (win.getEntry("username"))
            cursor.execute(query)
            result = cursor.fetchall()
            # Check if the username is already taken
            if result[0][0] == 0:
                query = "INSERT INTO User VALUES (\"%s\", \"%s\")" % (
                    win.getEntry("username"), win.getEntry("password"))
                cursor.execute(query)
                connection.commit()
            else:
                print("username is taken")
        else:
            print("inputs are not valid")
    # When submit is pressed
    elif name == "submit":
        if len(win.getEntry("username")) < 20 and len(win.getEntry("password")) < 20 and win.getEntry(
                "username").isalphanum() and win.getEntry("password").isalphanum():
            query = "SELECT Password FROM User WHERE Username == \"%s\"" % (win.getEntry("username"))
            cursor.execute(query)
            result = cursor.fetchall()
            if not len(result) == 0:
                if result[0][0] == win.getEntry("password"):
                    print("login successful")
                    win.stop()
                else:
                    print("Login failed")
            else:
                print("Login failed")
        else:
            print("inputs not valid")


win = gui("login")

win.addLabel("lb1", "login window")

# Set font properties
win.setBg("green")
win.setFg("white")
win.setFont(16)

# Create entry fields
win.addLabelEntry("username")
win.addSecretLabelEntry("password")

# Create buttons
win.addButtons(["submit", "register", "cancel"], press)

# Run gui
win.go()
