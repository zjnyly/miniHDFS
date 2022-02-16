# miniHDFS

This is a basic implementation of HDFS(Hadoop Distributed File System) using gRPC for the entire communication



![stucture-1](./pic/stucture-1.png)

## Run the code

### Activate the program

* First start the `NameNode`

  ```
  python3 NameNode.py
  ```

* Second, start 1~4 `DataNode`s, and choose 1~4 as name

  ```
  python3 DataNode.py
  ```

* Finally start 1~4 `Clients`, and register/login

  ```
  python3 Client.py
  ```

### Other codes

* Initialize the database

  ```
  python3 initializeDB.py
  ```

* Display the database data

  ```
  python3 showDatabase.py
  ```

* Update gRPC service

  ```
   python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. NameNode.proto
   python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. DataNode.proto
  ```

## Demo

![demo](./pic/demo.gif)

## Basic functions

* implemented some basic accessing operations like `ls`, `cd`, `mkdir`, `pwd`, using a filetree in json form

  <img src="./pic/image-20220216222607405.png" alt="image-20220216222607405" style="zoom:25%;" />

* Implemented  `upload` function

  ![image-20220216222118461](./pic/image-20220216222118461.png)

* Implemented  `download function

  ![image-20220216222153444](./pic/image-20220216222153444.png)

* Implemented  `delete` function

  ![image-20220216222215998](./pic/image-20220216222215998.png)

* Implemented  `copy` function

  ![image-20220216222520423](./pic/image-20220216222520423.png)

* Implemented  `atomic access` function

  ![image-20220216222325511](./pic/image-20220216222325511.png)

* Implemented  `permission management` function

  ![image-20220216222452056](./pic/image-20220216222452056.png)

* Implemented  `checksum` function

  ![image-20220216222538661](./pic/image-20220216222538661.png)

* Achieved final consistency

