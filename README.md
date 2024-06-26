
# Tìtanic Survival Calculator

Develop a Titanic Survivor Prediction web app using Python (FastAPI) and VueJS. Implement Dockerized services for the web application and prediction model. Ensure continuous integration with Gitlab CI, maintaining high test coverage with pytest and Cypress/Playwright. Follow Scrum methodology across three sprints, managing tasks and resources in Jira. Deliver a comprehensive presentation demonstrating the software, system architecture, and individual contributions.

1. **Titanic Survivor App**: A web application to predict the survival of passengers in the Titanic accident.
2. **Presentation**: A demonstration of the developed software, insights on the system architecture, and individual contributions.

## Requirements and Setup

### Prerequisites

- **Docker**: Ensure Docker is installed and running on your machine. [Docker Installation Guide](https://docs.docker.com/get-docker/)
- **Docker Compose**: Ensure Docker Compose is installed. [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

### Cloning Repositories

The project is divided into two repositories within the team's Gitlab group:

1. **Web Application Service Repository**: [Link to the repository]
2. **Prediction Model Service Repository**: [Link to the repository]

Clone both repositories to your local machine.

```sh
git clone <web_application_service_repo>
git clone <prediction_model_service_repo>
```

### Building and Running the Application

Navigate to the directory containing the Docker Compose file and run the following command to build and start the services:

```sh
docker-compose up --build
```

This command will:
- Build Docker images for both the web application service and the prediction model service.
- Start the services and make the web interface accessible at \`https://localhost:8080\`.

### Accessing the Web Application

Once the services are up and running, open your web browser and navigate to:

```
https://localhost:8080
```

## Application Structure

### Web Application

The web application consists of two main pages:

1. **Landing Page**: Provides a short explanation of the app's functionality and a link to the Survival Calculator.
2. **Survival Calculator**: Allows users to input passenger details and view survival predictions based on selected models.

#### Passenger Details Input

- **PClass**: First, Second, Third
- **Sex**: Male, Female
- **Age**: 0-100
- **Fare**: 0-500 $
- **Traveled Alone**: Yes, No
- **Embarked**: Cherbourg, Queenstown, Southampton

Users can view explanations for each input property and select prediction models from Random Forest, Decision Tree, KNN, Support Vector Machines, or Logistic Regression.

### Prediction Model Service

The prediction model service:
- Is written in Python using FastAPI.
- Uses models implemented as per the proof-of-concept notebook.
- Stores trained models as Pickle files.
- Exposes a RESTful API for prediction model inference.

## Testing and CI/CD

### Testing

- **Unit and Integration Tests**: Written using the pytest framework with a coverage requirement above 75%.
- **End2End Tests**: Written using Cypress or Playwright and automatically run in a nightly pipeline.

### Continuous Integration

- **Gitlab CI**: Docker images are built and pushed to the registry with each commit.
- **Pipeline Execution**: Unit and integration tests run on every commit, while End2End tests run nightly.

## Project Management

The project follows the Scrum framework with 3 sprints, each lasting 3 weeks. All non-code resources are managed in Jira.

## Contact Information

For any queries, contact Prof. Dr. Christoph Schober at christoph.schober@th-deg.de.

## Additional Notes

- Ensure to attend project meetings and the final presentation in Deggendorf.
- Follow the functional and non-functional requirements outlined in the project document.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
