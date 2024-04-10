# Job Application Tracker

The Job Application Tracker is a web application built with Flask that allows users to track and manage their job applications. It provides a user-friendly interface for adding, editing, and deleting job applications, as well as viewing a list of all submitted applications.

## Features

- Add new job applications with details such as company, location, job description, resume, and cover letter links
- Edit existing job applications
- Delete job applications
- View a list of all submitted job applications
- Select applicant names from a predefined list

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/job-application-tracker.git
   ```

2. Navigate to the project directory:

   ```
   cd job-application-tracker
   ```

3. Create a `.env` file by copying the example file:

   ```
   cp .env.example .env
   ```

   Edit the `.env` file and set the required environment variables according to your needs.

4. Create an `applicant_names.yml` file by copying the example file:

   ```
   cp config/applicant_names.yml.example config/applicant_names.yml
   ```

   Edit the `applicant_names.yml` file and add or modify the list of applicant names as desired.

5. Adjust the exposed port in the `docker-compose.yml` file if needed (currently set to `5001`).

6. Build and run the Docker container:

   ```
   docker-compose up --build
   ```

7. Access the application in your web browser at `http://localhost:5001`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
