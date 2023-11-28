import mysql.connector
from mysql.connector import errorcode

# Function to handle MySQL connection and cursor creation
def connect_to_database():
    try:
        # Connect to the MySQL server
        cnx = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost:3306',
            database='pysports'
        )

        # Create a cursor object using the connection
        cursor = cnx.cursor()

        return cnx, cursor

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
        
        # Exit the script if there's an error
        exit()

# Function to close the cursor and connection to the database
def close_connection(cursor, cnx):
    cursor.close()
    cnx.close()

# Main function to execute queries and display results
def main():
    # Connect to the database
    cnx, cursor = connect_to_database()

    try:
        # Query for the team table
        team_query = "SELECT team_id, team_name, mascot FROM team"
        cursor.execute(team_query)

        # Display results for the team table
        print("Team Table:")
        for (team_id, team_name, mascot) in cursor:
            print(f"Team ID: {team_id}, Team Name: {team_name}, Mascot: {mascot}")

        # Query for the player table
        player_query = "SELECT player_id, first_name, last_name, team_id FROM player"
        cursor.execute(player_query)

        # Display results for the player table
        print("\nPlayer Table:")
        for (player_id, first_name, last_name, team_id) in cursor:
            print(f"Player ID: {player_id}, First Name: {first_name}, Last Name: {last_name}, Team ID: {team_id}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        close_connection(cursor, cnx)

if __name__ == "__main__":
    # Run the main function if the script is executed
    main()
