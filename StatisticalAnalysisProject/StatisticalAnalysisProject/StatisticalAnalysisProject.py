import os
import tkinter as tk
import statistics
import numpy as np
from matplotlib import pyplot as plt

 
root= tk.Tk()
root.title("Statistical Analysis")
root.resizable(0,0)

list1 = [] 
canvas1 = tk.Canvas(root, width = 600, height = 450, bg = 'dark slate gray', relief = 'raised')
canvas1.pack()


def pieChart(mylist1,*args):
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    plt.pie(mylist1, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title('Pie Chart') 
    plt.show()

def lineChart(mylist1,*args):
    plt.plot(mylist1)
    plt.title('Line Chart')
    plt.show()

def barChart(mylist1,*args):
    ypos = np.arange(int(len(mylist1))) 
    plt.bar(ypos,mylist1, align='center', alpha=0.5)
    plt.title('Bar Chart')
    plt.show()

    
listLabel = tk.Label(root, text='Enter the Variables seperated by *Commas*:',fg = 'cyan', bg='dark slate gray')
listLabel.config(font=('helvetica', 10))
canvas1.create_window(150, 50, window=listLabel)

entry_text = tk.StringVar()
listEntry = tk.Entry (root, width=27, textvariable = entry_text)
canvas1.create_window(400, 50, window=listEntry)

def requiredField(): 
     list1.clear()
     if len(listEntry.get()) == 0: 
         new_text = "Required Field"
         listEntry.delete(0, tk.END)
         listEntry.insert(0, new_text)

     else :

         # convert to the list
         list = listEntry.get().split (",")
         
         # convert each element as integers
        
         for i in list:
         	list1.append(int(i))

     # set text boxes for mean median mode variance
     
     # Mean 

     meanLabel = tk.Label(root, text='mean : ',fg = 'cyan', bg='dark slate gray')
     meanLabel.config(font=('helvetica', 10))
     canvas1.create_window(100, 120, window=meanLabel)
     
     mean_entry_text = tk.StringVar()
     meanEntry = tk.Entry (root, width=20, textvariable = mean_entry_text)
     canvas1.create_window(200, 120, window=meanEntry)
     
     meanEntry.delete(0, tk.END)
     meanEntry.insert(0, statistics.mean(list1))

      # Median 

     medianLabel = tk.Label(root, text='median : ',fg = 'cyan', bg='dark slate gray')
     medianLabel.config(font=('helvetica', 10))
     canvas1.create_window(100,150, window=medianLabel)
     
     median_entry_text = tk.StringVar()
     medianEntry = tk.Entry (root, width=20, textvariable = median_entry_text)
     canvas1.create_window(200,150, window=medianEntry)

     medianEntry.delete(0, tk.END)
     medianEntry.insert(0, statistics.median(list1))
       
     # Mode

     modeLabel = tk.Label(root, text='mode : ',fg = 'cyan', bg='dark slate gray')
     modeLabel.config(font=('helvetica', 10))
     canvas1.create_window(100, 180, window=modeLabel)
     
     mode_entry_text = tk.StringVar()
     modeEntry = tk.Entry (root, width=20, textvariable =  mode_entry_text)
     canvas1.create_window(200, 180, window=modeEntry)

     try : 
          statistics.mode(list1)
          modeEntry.delete(0, tk.END)
          modeEntry.insert(0, statistics.mode(list1)) 
          
     except ValueError:  
          modeEntry.delete(0, tk.END)
          modeEntry.insert(0, "No Mode Found")  

     # Variance
     varianceLabel = tk.Label(root, text='variance : ', fg = 'cyan', bg='dark slate gray')
     varianceLabel.config(font=('helvetica', 10))
     canvas1.create_window(100, 210, window=varianceLabel)
         
     variance_entry_text = tk.StringVar()
     varianceEntry = tk.Entry (root, width=20, textvariable =  variance_entry_text)
     canvas1.create_window(200, 210, window=varianceEntry)

     try:
           statistics.variance(list1)
           varianceEntry.delete(0, tk.END)
           varianceEntry.insert(0,  statistics.variance(list1))  

     except ValueError:
          varianceEntry.delete(0, tk.END)
          varianceEntry.insert(0,  "No variance Found")  

     pieChartButton = tk.Button(text=' Pie Graph',command=lambda:pieChart(list1),bg='cyan', fg='black', font=('helvetica', 10, 'bold'))
     canvas1.create_window(300, 430, window=pieChartButton)

     lineChartButton = tk.Button(text='Line Graph',command=lambda:lineChart(list1),bg='cyan', fg='black', font=('helvetica', 10, 'bold'))
     canvas1.create_window(420, 430, window=lineChartButton)

     barChartButton = tk.Button(text=' Bar Graph',command=lambda:barChart(list1),bg='cyan', fg='black', font=('helvetica', 10, 'bold'))
     canvas1.create_window(540, 430, window=barChartButton)


addButton = tk.Button(text='    Add    ',command= requiredField,bg='cyan', fg='black', font=('helvetica', 10, 'bold'))
canvas1.create_window(550, 50, window=addButton)



root.mainloop()
os.system("pause")


