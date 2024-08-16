# Connect to your mongo database.

1. In the left settings bar, go to **Network Access** and check if your IP address has been added successfully. You should see a green dot in the status column. If your IP address is not added, you will not be able to connect to the database from your device.
![image](./assets/8-Atlas.png)
2. In the left settings bar, go to **Clusters** and press **Connect** button. Then from **Connect to your application** choose **Drivers**.
![image](./assets/9-Atlas.png)
![image](./assets/10-Atlas.png)
3. Now copy the connection string from step 3.
![image](./assets/11-Atlas.png)
4. Create a new variable in the `.envrc` file in your project. Remember to replace the password placeholder with your database user's password in the connection string. `export MONGODB_URI="your_connection_string"`
5. Install plugin for mongodb on youd IDE.
    * PyCharm - [tutorial](https://www.jetbrains.com/help/pycharm/mongodb.html#general_tab)

    * Visual studio code - [tutorial](https://code.visualstudio.com/docs/azure/mongodb)
6. Connect to your database from python using beanie framework.

