import numpy as np
# Marix Calculator
try:
    a=input("Please enter number of rows for matrix A: ")
    b=input("Please enter number of columns for the matrix A: ")
    A=input("Please enter the number of rows for matrix B: ")
    B=input("Please enter the number of columns for matrix B: ")
    r=int(a) * int(b)
    r1=int(A) * int(B)
    arr=np.arange(1,r+1).reshape(int(a), int(b))
    arr1=np.arange(1,r1+1).reshape(int(A), int(B))
    print("Matrix A:")
    print(arr)
    print("Matrix B:")
    print(arr1)
    choice=0
    while True:
        print("Doing Matrix Calculations...\n Please Enter Your Choice of the following: ")
        print("1. Addition")
        print("2. Multiplication")
        print("3. determinant")
        print("4. Transpose")
        print("5. To enter statistical analyzer")
        print("6. Exit")
        
        try:
            choice=int(input("Enter your choice: "))
            if choice==1:
                print("Addition of Matrix A and B:")
                print(arr+arr1)
            elif choice==2:
                print("Multiplication of Matrix A and B:")
                print(np.dot(arr, arr1))
            elif choice==3:
                print("Determinant of Matrix A:")
                print(np.linalg.det(arr))  
                print("Determinant of Matrix B:")
                print(np.linalg.det(arr1))
            elif choice==4:
                print("Transpose of Matrix A:")
                print(np.transpose(arr))
                print("Transpose of Matrix B:")
                print(np.transpose(arr1))
            elif choice==5:
                c=int(input("choose an array for its statistical analysis\n press 1 for array A\n press 2 for array B\n"))
                if c==1:
                    print("Statistical Analysis of Matrix A:")
                    print("Mean: ", np.mean(arr))
                    print("Median: ", np.median(arr))
                    print("correlation: ", np.corrcoef(arr))
                elif c==2:
                    print("Statistical Analysis of Matrix B:")
                    print("Mean: ", np.mean(arr1))
                    print("Median: ", np.median(arr1))
                    print("correlation: ", np.corrcoef(arr1))
                else:
                    print("Invalid choice for statistical analysis.")  
            elif choice==6:
                print("Exiting the program.")
                break              
            else:
                print("invalid choice, please try again.")

        except Exception as e:
            print(f"An Error Occurred: {e}  Please try again.")
except Exception as e:
    print(f"An Error Occurred: {e}  exiting prpogram.")            

