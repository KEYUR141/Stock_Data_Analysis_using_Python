# Stock_Data_Analysis_using_Python

<h1>Stock Data Analysis</h1>
<p>For my stock data analysis project using Python, the assignment involves three main steps. First, I need to create a table in an MS SQL Server database and insert data for one ticker symbol into this table using Python. This involves setting up the database connection in MS SQL Server Management Studio and ensuring the data is successfully inserted. Second, I will analyze the data using Python and create an investing or trading strategy. The recommended strategy for those unfamiliar is the simple moving average (SMA) crossover strategy, which identifies potential buy and sell signals based on the crossover of short-term and long-term moving averages. Finally, I will submit the results of how my strategy is performing. To ensure data integrity, I will write a unit testing module with pytest to validate that the input data meets specified criteria: the Open, High, Low, and Close columns should be decimals, the Volume column should be an integer, the Instrument column should be a string, and the Datetime column should be a datetime type. By completing these steps, I aim to effectively demonstrate my ability to handle, test, and analyze stock data using Python and MS SQL Server.</p>

<div class='Data_Insert'>
    <h1>Inserting Data into MS SQL Server Using Python</h1>
    <p>
        This project demonstrates how to insert stock data into an MS SQL Server database using Python and the `pyodbc` library. The process involves establishing a connection to the database, reading data from an Excel file, creating a table in the database, and inserting the data into the table. Below are the steps in detail:
    </p>
    
  <h2>Steps</h2>
    <ol>
        <li>
            <strong>Import Libraries:</strong>
            <p>First, import the required libraries, `pyodbc` for database connection and `pandas` for data manipulation.</p>
            <pre><code>import pyodbc
import pandas as pd
            </code></pre>
        </li>
        <li>
            <strong>List Available Drivers:</strong>
            <p>Check the available ODBC drivers on your system to ensure the correct driver is installed.</p>
            <pre><code>pyodbc.drivers()</code></pre>
        </li>
        <li>
            <strong>Establish a Connection:</strong>
            <p>Establish a connection to the MS SQL Server database using the `ODBC Driver 17 for SQL Server` and Windows Authentication.</p>
            <pre><code>conn = pyodbc.connect(
    Trusted_Connection = "Yes",
    Driver = '{ODBC Driver 17 for SQL Server}',
    Server = "DESKTOP-D9QH4PH",
    Database = "HINDALCO"
)
cursor = conn.cursor()
            </code></pre>
        </li>
        <li>
            <strong>Read Data from Excel:</strong>
            <p>Read the stock data from an Excel file into a pandas DataFrame.</p>
            <pre><code>df = pd.read_excel(r'C:\Users\DELL\Downloads\HINDALCO_1D.xlsx')
df.head()
df.columns
            </code></pre>
        </li>
        <li>
            <strong>Create Table in Database:</strong>
            <p>Execute an SQL command to create a table named `stock_data` in the `HINDALCO` database with the required columns and data types.</p>
            <pre><code>cursor.execute("""
    CREATE TABLE stock_data (
        [datetime] DATETIME,
        [close] DECIMAL(10,2),
        [high] DECIMAL(10,2),
        [low] DECIMAL(10,2),
        [open] DECIMAL(10,2),
        [volume] INT,
        [instrument] VARCHAR(50)
    )
""")
            </code></pre>
        </li>
        <li>
            <strong>Insert Data into the Table:</strong>
            <p>Loop through each row in the DataFrame and execute an SQL `INSERT` statement to add the data to the `stock_data` table.</p>
            <pre><code>for row in df.itertuples(index=False):
    cursor.execute("""
        INSERT INTO HINDALCO.dbo.stock_data (datetime, [close], high, low, [open], volume, instrument)
        VALUES(?,?,?,?,?,?,?)""",
        (row.datetime,
        row.close,
        row.high,
        row.low,
        row.open,
        row.volume,
        row.instrument,
        )
    )
conn.commit()
            </code></pre>
        </li>
        <li>
            <strong>Close the Connection:</strong>
            <p>Finally, close the connection to the database.</p>
            <pre><code>conn.close()</code></pre>
        </li>
    </ol>
    
</div>

<div class='Moving_Average'>
  

</div>
