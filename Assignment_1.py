

def add_info():
    id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    dept = input("Department Name: ")

    d = {
        "id" : id,
        "name" : name,
        "dept" : dept
    }
    
    with open("Document.txt", "a") as f:
        f.write(f"{d}\n")


#add_info()

def view_all():
    with open("Document.txt", "r") as f:
        lines = f.readlines()

        for line in lines:
            print(line)

#view_all()

def search():
    id = input("Enter Student ID: ")

    with open("Document.txt", "r") as f:
            
        lines = f.readlines()

        #print(lines)

        for line in lines:

            dic_line = eval(line)

            if ( id == dic_line["id"]):

                print(line)
                break

        
#search()

def delete():

    id = input("Enter ID, you want to delete: ")

    with open("Document.txt", "r") as f:
            
            lines = f.readlines()

            #print(lines)

            idx = 0

            for line in lines:

                dic_line = eval(line)

                if ( id == dic_line["id"]):

                    del lines[idx]

                
                idx += 1

            #print(lines)

            with open("Document.txt", "w") as f:
                f.write("")

            for line in lines:
                with open("Document.txt", "a") as f:
                    f.write(line)
        
    print("Successfully Deleted...")




while(True):
    print("1. Add Student Informnation")
    print("2. View")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            add_info()

        case 2:
            view_all()

        case 3:
            search()

        case 4:
            delete()

        case 5:
            break

        case _:
            print("Invalid Choice....")


#print(std_list)