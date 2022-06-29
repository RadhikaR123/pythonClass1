


# try:
#     f= open('testfile.txt')
# # except exception as e:
# #     print('error name is ', e)
# except FileNotFoundError as e:
#     print(e)
# else:
#     print(f.read())
#     f.close()
# finally:
#     print("you didit all correct....")




try:
  f = open("test_file.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")


#   dfgds