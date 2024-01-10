from pymongo import MongoClient
import customtkinter
import json

'''
Dependencies:

pip install pymongo

pip install customtkinter

pip install tkinter

pip install packaging

'''
customtkinter.set_appearance_mode("Dark")


myclient = MongoClient("MongoDB Connection String")
mydb = myclient["rentacar"]
rentCol = mydb["rent"]
userCol = mydb["user"]

window = customtkinter.CTk()
window.title("")
window.resizable(False, False)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

container = customtkinter.CTkFrame(
    window,
    fg_color="#333",
    height=60,
)
container.grid(row=0, column=0, padx=10, pady=10,sticky="nwse")

button = customtkinter.CTkButton(
    container, text="Create", command=lambda: frameInit("Create")
)
button.grid(row=0, column=0, padx=5, pady=5)
button = customtkinter.CTkButton(
    container, text="Read", command=lambda: frameInit("Read")
)
button.grid(row=1, column=0, padx=5, pady=5)
button = customtkinter.CTkButton(
    container, text="Update", command=lambda: frameInit("Update")
)
button.grid(row=2, column=0, padx=5, pady=5)
button = customtkinter.CTkButton(
    container, text="Delete", command=lambda: frameInit("Delete")
)
button.grid(row=3, column=0, padx=5, pady=5)

label = customtkinter.CTkLabel(container, text="Collection")
label.grid(row=4, column=0)
combobox = customtkinter.CTkComboBox(
    container, values=["Rent", "User"], command=print, state="readonly"
)
combobox.set("User")
combobox.grid(rowspan=4, row=8, column=0)


def is_on(var):
    return var == "on"

# Create Document Entries

def frameInit(Operation):
    operation_frame = customtkinter.CTkScrollableFrame(window ,width=300, height=500 ,   fg_color="#222")
    operation_frame.grid(row=0, column=1, padx=5, pady=10, sticky="nwse")

    choice = combobox.get()
    if choice == "Rent":
        obj = readDoc(rentCol,{})
        currentCol = rentCol
    if choice == "User":
        obj = readDoc(userCol,{})
        currentCol = rentCol
    if Operation == "Create":

        user_entry1 = customtkinter.CTkEntry(operation_frame, placeholder_text="userid")
        user_entry2 = customtkinter.CTkEntry(operation_frame, placeholder_text="Nome")
        user_entry3 = customtkinter.CTkEntry(operation_frame, placeholder_text="Email")
        user_entry4 = customtkinter.CTkEntry(operation_frame, placeholder_text="Idade")
        user_entry5 = customtkinter.CTkEntry(operation_frame, placeholder_text="Rua")
        user_entry6 = customtkinter.CTkEntry(operation_frame, placeholder_text="Cidade")
        user_entry7 = customtkinter.CTkEntry(operation_frame, placeholder_text="Pais")
        user_entry8 = customtkinter.CTkEntry(operation_frame, placeholder_text="Interesses",width=220)

        car_entry1 = customtkinter.CTkEntry(operation_frame, placeholder_text="carId")
        car_entry2 = customtkinter.CTkEntry(operation_frame, placeholder_text="Modelo")
        car_entry3 = customtkinter.CTkEntry(operation_frame, placeholder_text="Marca")
        car_entry4 = customtkinter.CTkEntry(operation_frame, placeholder_text="Ano")
        car_entry5 = customtkinter.CTkEntry(operation_frame, placeholder_text="Preço")
        car_entry6 = customtkinter.CTkEntry(operation_frame, placeholder_text="Extras",width=220)
        car_entry7 = customtkinter.CTkEntry(operation_frame, placeholder_text="Categoria")


        if combobox.get() == "Rent":

            #Inputs para criar um carro 

            car_entry1.grid(row=1, column=0, padx=10, pady=(10, 10))
            car_entry2.grid(row=2, column=0, padx=10, pady=(10, 10))
            car_entry3.grid(row=3, column=0, padx=10, pady=(10, 10))
            car_entry4.grid(row=4, column=0, padx=10, pady=(10, 10))
            car_entry5.grid(row=6, column=0, padx=10, pady=(10, 10))
            car_entry6.grid(row=7, column=0, padx=0, pady=(0, 0))
            label = customtkinter.CTkLabel(operation_frame, text="(separados por virgulas!)",text_color=("grey"),font=("Arial",12))
            label.grid(row=8, column=0)
            car_entry7.grid(row=9, column=0, padx=10, pady=(10, 10))
            car_button = customtkinter.CTkButton(
                operation_frame,
                text="Create",
                command=lambda: createDoc(
                    userCol,
                    {
                        "carId": car_entry1.get(),
                        "model": car_entry2.get(),
                        "make": car_entry3.get(),
                        "year": int(car_entry4.get()),
                        "price": int(car_entry5.get()),
                        "available": True,
                        "features": car_entry6.get().split(","),
                        "carType": car_entry7.get(),
                    },
                ),
            )
            car_button.grid(row=10, column=0,pady=(10, 10))

        elif combobox.get() == "User":

            #Inputs para criar um user 

            user_entry1.grid(row=1, column=0, padx=10, pady=(10, 10))
            user_entry2.grid(row=2, column=0, padx=10, pady=(10, 10))
            user_entry3.grid(row=3, column=0, padx=10, pady=(10, 10))
            user_entry4.grid(row=4, column=0, padx=10, pady=(10, 10))
            user_label = customtkinter.CTkLabel(operation_frame, text="Endereço:")
            user_label.grid(row=5, column=0)
            user_entry5.grid(row=6, column=0, padx=10, pady=(10, 10))
            user_entry6.grid(row=7, column=0, padx=10, pady=(10, 10))
            user_entry7.grid(row=8, column=0, padx=10, pady=(10, 10))
            user_entry8.grid(row=9, column=0, padx=10,pady=(10, 0))
            label = customtkinter.CTkLabel(operation_frame, text="(separados por virgulas!)")
            label.grid(row=10, column=0)
            user_button = customtkinter.CTkButton(
                operation_frame,
                text="Create",
                command=lambda: createDoc(
                    userCol,
                    {
                        "userId": user_entry1.get(),
                        "nome": user_entry2.get(),
                        "email": user_entry3.get(),
                        "idade": int(user_entry4.get()),
                        
                        "endereco":{"rua": user_entry5.get(), "cidade": user_entry6.get(),"pais": user_entry7.get()},

                        "interesses": user_entry8.get().split(","),
                        "ativo": True,
                    },
                ),
            )
            user_button.grid(row=11, column=0,pady=(10, 10))
    elif Operation == "Read":

        for index, document in enumerate(obj):
            
            container = customtkinter.CTkFrame(
                operation_frame,
                fg_color="#333",
                width=200,
            )
            container.grid(row=index, column=0, padx=2, pady=2)
            if "carId" in document.keys():
                label = customtkinter.CTkLabel(
                    container, text="ID: " + document["carId"],
                    text_color=checkactive(document["available"])
                )
                label.grid(row=0, column=0, padx=1)

                label = customtkinter.CTkLabel(
                    container, text="Marca: " + document["make"]
                )
                label.grid(row=1, column=0, padx=1)
                label = customtkinter.CTkLabel(
                    container, text="Model: "+ document["model"]
                )
                label.grid(row=2, column=0, padx=1)
                label = customtkinter.CTkLabel(
                    container, text="Preço: "+ str(document["price"]) + " $" 
                )
                label.grid(row=3, column=0, padx=1)

                label = customtkinter.CTkLabel(
                    container, text="Ano: "+ str(document["year"]) 
                )
                label.grid(row=4, column=0, padx=1)
            if "userId" in document.keys():
                
                label = customtkinter.CTkLabel(
                    container,
                    text=document["_id"],
                    text_color=checkactive(document["ativo"]),
                )
                label.grid(row=0, column=0, padx=1)

                label = customtkinter.CTkLabel(
                    container, text="User ID: " + document["userId"]
                )
                label.grid(row=1, column=0, padx=1, pady=1)
                
                
                label = customtkinter.CTkLabel(
                    container, text="Nome: " + document["nome"]
                )
                label.grid(row=2, column=0, padx=1, pady=1)

                label = customtkinter.CTkLabel(
                    container, text="Interesses:"
                )
                label.grid(row=3, column=0, padx=1)
                
                if "interesses" in document:
                    label = customtkinter.CTkLabel(
                        container, text=" | ".join(document["interesses"])
                    )
                    label.grid(row=4, column=0, padx=1, pady=1)
                

                label = customtkinter.CTkLabel(
                    container, text="Endereço:"
                )
                label.grid(row=5, column=0, padx=1)

                label2 = customtkinter.CTkLabel(
                    container, text=" | ".join(document["endereco"].values())
                )
                label2.grid(row=6, column=0, padx=1, pady=1)
    elif Operation == "Update":
        objlist = list(obj)
        results = []

        switch_var = customtkinter.StringVar(value="on")
        switch_var2 = customtkinter.StringVar(value="on")

        def switch_event():
            print("Active | switch toggled, current value:", is_on(switch_var.get()))
            print("Available | Switch toggled, current value:", is_on(switch_var2.get()))

        uentry2 = customtkinter.CTkEntry(operation_frame, placeholder_text="Nome")
        uentry3 = customtkinter.CTkEntry(operation_frame, placeholder_text="Email")
        uentry4 = customtkinter.CTkEntry(operation_frame, placeholder_text="Idade")
        uentry5 = customtkinter.CTkEntry(operation_frame, placeholder_text="Rua")
        uentry6 = customtkinter.CTkEntry(operation_frame, placeholder_text="Cidade")
        uentry7 = customtkinter.CTkEntry(operation_frame, placeholder_text="Pais")
        uentry8 = customtkinter.CTkEntry(operation_frame, placeholder_text="Interesses",width=220)
        switch = customtkinter.CTkSwitch(operation_frame, text="Ativo?", command=switch_event,
                            variable=switch_var, onvalue="on", offvalue="off")
        
        centry2 = customtkinter.CTkEntry(operation_frame, placeholder_text="Modelo")
        centry3 = customtkinter.CTkEntry(operation_frame, placeholder_text="Marca")
        centry4 = customtkinter.CTkEntry(operation_frame, placeholder_text="Ano")
        centry5 = customtkinter.CTkEntry(operation_frame, placeholder_text="Preço")
        centry6 = customtkinter.CTkEntry(operation_frame, placeholder_text="Extras",width=220)
        centry7 = customtkinter.CTkEntry(operation_frame, placeholder_text="Categoria")
        switch2 = customtkinter.CTkSwitch(operation_frame, text="Disponivel?", command=switch_event,
                            variable=switch_var2, onvalue="on", offvalue="off")

        for doc in objlist:
            if "userId" in doc.keys():
                results.append(doc["nome"])
                doclist = customtkinter.CTkComboBox(
                operation_frame, values=results, command=print, state="readonly"
                )
                doclist.set("Select a Document!!")
                doclist.grid(row=0, column=0)
                uentry2.grid(row=2, column=0, padx=10, pady=(10, 10))
                uentry3.grid(row=3, column=0, padx=10, pady=(10, 10))
                uentry4.grid(row=4, column=0, padx=10, pady=(10, 10))
                label = customtkinter.CTkLabel(operation_frame, text="Endereço:")
                label.grid(row=5, column=0)
                uentry5.grid(row=6, column=0, padx=10, pady=(10, 10))
                uentry6.grid(row=7, column=0, padx=10, pady=(10, 10))
                uentry7.grid(row=8, column=0, padx=10, pady=(10, 10))
                uentry8.grid(row=9, column=0, padx=10, pady=(10, 0))
                switch.grid(row=10, column=0)
                endereco = {"rua": uentry5.get(), "cidade": uentry6.get(), "pais": uentry7.get()}
                
                def my_dict():
                    doc = {}
                    if uentry2.get() != '':
                        doc["nome"] = uentry2.get()
                    if uentry3.get() != '':
                        doc["email"] = uentry3.get()
                    if uentry4.get() != '':
                        doc["idade"] = int(uentry4.get())
                    if uentry5.get() != '':
                        doc["rua"] = uentry5.get()
                    if uentry6.get() != '':
                        doc["cidade"] = uentry6.get()
                    if uentry7.get() != '':
                        doc["pais"] = uentry7.get()
                    if uentry8.get() != '':
                        doc["interesses"] = uentry8.get().split(",")
                    doc["ativo"] = is_on(switch_var.get())
                    return doc


                button = customtkinter.CTkButton(
                    operation_frame,
                    text="Update",
                    command=lambda: updateDoc(userCol,my_dict(),{"nome":doclist.get()}),
                )
                button.grid(row=11, column=0)
            if "carId" in doc.keys():
                results.append(doc["carId"])
                doclist = customtkinter.CTkComboBox(
                operation_frame, values=results, command=print, state="readonly"
                )
                doclist.set("Select a Document!!")
                doclist.grid(row=0, column=0)
                centry2.grid(row=2, column=0, padx=10, pady=(10, 10))
                centry3.grid(row=3, column=0, padx=10, pady=(10, 10))
                centry4.grid(row=4, column=0, padx=10, pady=(10, 10))
                centry5.grid(row=6, column=0, padx=10, pady=(10, 10))
                centry6.grid(row=7, column=0, padx=0, pady=(0, 0))
                label = customtkinter.CTkLabel(operation_frame, text="(separados por virgulas!)",text_color=("grey"),font=("Arial",12))
                label.grid(row=8, column=0)
                centry7.grid(row=9, column=0, padx=10, pady=(10, 10))
                switch2.grid(row=10, column=0)

                def my_dict():
                    doc = {}
                    if centry2.get() != '':
                        doc["model"] = centry2.get()
                    if centry3.get() != '':
                        doc["make"] = centry3.get()
                    if centry4.get() != '':
                        doc["year"] = int(centry4.get())
                    if centry5.get() != '':
                        doc["price"] = int(centry5.get())
                    if centry6.get() != '':
                        doc["features"] = centry6.get().split(",")
                    if centry7.get() != '':
                        doc["carType"] = centry7.get()
                    doc["available"] = is_on(switch_var2.get())
                    return doc

                car_button = customtkinter.CTkButton(
                    operation_frame,
                    text="Update",
                    command=lambda: updateDoc(rentCol,my_dict(),{"carId":doclist.get()})
                )
                car_button.grid(row=11, column=0,pady=(10, 10))
    elif Operation == "Delete":
        objlist2 = list(obj)
        results = []
        for doc in objlist2:
            if "userId" in doc.keys():
                results.append(doc["nome"])
                doclist = customtkinter.CTkComboBox(
                    operation_frame, values=results, command=print, state="readonly"
                )
                doclist.set("Select a Document!!")
                doclist.grid(row=0, column=0)
                user_button = customtkinter.CTkButton(
                    operation_frame,
                    text="Delete",
                    command=lambda: deleteDoc(userCol,{"nome":doclist.get()}),
                    fg_color="red",
                    hover_color="#e22"
                )
                user_button.grid(row=11, column=0,pady=(10, 10))
            if "carId" in doc.keys():
                results.append(doc["carId"])
                doclist = customtkinter.CTkComboBox(
                    operation_frame, values=results, command=print, state="readonly"
                )
                doclist.set("Select a Document!!")
                doclist.grid(row=0, column=0)
                car_button = customtkinter.CTkButton(
                    operation_frame,
                    text="Delete",
                    command=lambda: deleteDoc(rentCol,{"carId":doclist.get()}),
                    fg_color="red",
                    hover_color="#e22"
                )
                car_button.grid(row=11, column=0,pady=(10, 10))


def checkactive(ativo):
    if ativo:
        return "green"
    else:
        return "red"

def createDoc(coll, doc):
    print(coll.insert_one(doc))

def readDoc(collection, config):
    return collection.find({})

def updateDoc(coll,doc,filter):
    print(coll.update_one(filter,{"$set":doc}))

def deleteDoc(coll,filter):
    print(coll.delete_one(filter))

window.mainloop()
