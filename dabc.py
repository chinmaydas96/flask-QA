import os 
  
# Function to rename multiple files 
def main(): 
      
    for filename in os.listdir():
        dst = filename.replace(': ', ':')
        dst = dst.replace(' ', '_')
        dst = dst.replace('(', '')
        dst = dst.replace(')', '')
        print(filename, dst)
        #import pdb;pdb.set_trace();
        src =filename  
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
