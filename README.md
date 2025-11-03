# Inventory

[![License](https://img.shields.io/badge/license-MIT-red.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.13+-yellow)
![React](https://img.shields.io/badge/frontend-React-purple)
![FastAPI](https://img.shields.io/badge/backend-FastAPI-green)

## Table of Content
- [About](#about)
- [Features](#features)
- [Tech Stack](#tech_stack)
- [Requirement](#requirement)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api_endpoints)
- [Contributing](#contributing)
- [License](#license)


## About
This system helps keep track of sales and purchases and provides clear data which helps in making accurate decisions

## Features
- Add, edit and delete products
- Realtime stock updates
- Export reports to csv, json and xml
- RESTful API integration

## Tech Stack
- **Frontend:** React, Bootstrap
- **Backend:** FastAPI
- **Database:** PostgreSQL
- **Authentication:** JWT

## Requirement
`Frontend: `
```bash
    node v24.8.0
    npm v11.6.0
```
`Backend: `
```bash
    python 3.11
```

## Installation
`Clone the repository: `
``` bash
    git clone https://github.com/lokiturner5-afk/Inventory.git
    cd inventory
```
`Install Dependencies`
```bash
    npm install
    pip install -r requirements.txt
```
`Run the backend server`
```bash
    uvicorn main:app --reload
```
`Run the frontend`
```bash
    npm run dev
```

## **Usage**

## Example API usage
```bash
    GET /api/get-products
    POST /api/add-product
```

## Contributing
Contributions are welcome!  
Please fork the repository and submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Contact
**Developer:** Loki  
**Email:** lokiturn5@gmail.com
