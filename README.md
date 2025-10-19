# AI Diet and Meal Planner

## Project Overview:

**AI Diet and Meal Planner** is a Python-based backend service that leverages **multi-agent workflows** to help you plan personalized meals based on available ingredients, dietary preferences, and nutritional needs. The system is built using **FastAPI** for structuring and exposing REST APIs, and integrates **Large Language Models (LLMs)** to assist with recipe recommendations, meal planning, and nutritional analysis.

With the AI Diet and Meal Planner, you get an AI-powered sous-chef that helps you choose recipes based on what you have in your kitchen. It can filter meals by diet type, optimize your meal plan according to your health goals, and guide you through the preparation process with structured step-by-step instructions.

---

## Features

- **Multi-Agent System**: Design various agents that work together to analyze ingredients, suggest recipes, and create meal plans.
- **REST APIs**: Expose agent services via REST APIs using FastAPI, allowing easy interaction and integration.
- **LLM Integration**: Interact with LLM providers using customized prompts to generate recipe ideas, suggest ingredients, and provide cooking instructions.
- **Prompt Engineering**: Implement advanced prompt engineering techniques to refine recipe generation and meal planning for specific diets.
- **Diet Customization**: Filter recipes by dietary needs such as vegetarian, keto, low-carb, etc.
- **Nutritional Analysis**: Plan and recommend meals that fit your available ingredients.
- **JSON Output**: Structured JSON output from LLMs for easy consumption and integration.
- **Docker Support**: The project includes a Dockerfile for easy containerization and deployment.

---

## Tools & Technologies

This project utilizes several tools and libraries to create the multi-agent meal planner:

- **FastAPI**: To expose REST APIs and structure the agents' workflows.
- **Langchain**: For orchestrating interactions between LLMs and APIs to generate recipes and meal plans.
- **Pydantic**: For data validation and serialization, ensuring inputs and outputs are correctly formatted.
- **Uvicorn**: As the ASGI server to run the FastAPI application.
- **Docker**: To containerize the application and make it easy to deploy and scale.
- **Groq API**: Used for accessing structured recipe data, ingredients, and generating personalized meal suggestions based on user input. GROq's data models are used for retrieving recipe information and generating meal plans and dietary suggestions.
- **LLM Integration**: The system is designed to interact with any **Large Language Models (LLMs)** to dynamically generate personalized meal plans, recipe ideas, and nutritional information. The specific LLM used (GROq) can be easily switched by modifying the `llm_client.py` and `.env` file, making the application flexible to use different LLM providers.

---

## Installation

To get started with the **AI Diet and Meal Planner**, you need to set up the environment and install the required dependencies.

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/AI-Diet-Meal-Planner.git
   cd AI-Diet-Meal-Planner


2. **Create a virtual environment (recommended):**
     ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`


3. ** Install dependencies:**
     ```bash
    pip install -r requirements.txt
   
4. ** Create a .env file in the root directory of the project with the following content:**
     ```bash
    GROQ_API_KEY=your_groq_api_key_here
   
Replace your_groq_api_key_here with your actual Groq API key.

5. **Run the FastAPI server:**
    ```bash
   uvicorn main:app --reload
This will start the FastAPI server on http://127.0.0.1:8000.

---

## Docker

This project includes a Dockerfile to containerize the application for easy deployment.

## Building the Docker Image
To build the Docker image, run:

    docker build -t ai-diet-meal-planner .

## Running the Docker Container
To run the Docker container, execute:
    
    docker run --env-file .env --ai-diet-meal-planner -p 8000:8000 ai-diet-meal-planner:latest 

This will start the FastAPI server within a Docker container and expose it on port 8000 on your local machine.

---


## API Endpoints
### 1. **Root Endpoint**
- **GET** `/`
- **Summary**: Returns a simple confirmation of the API status.

**Response**:

    {
      "message": "AI Diet and Meal Planner API is up and running!"
    }
---
### 2. Inventory Endpoint
- **POST** /inventory/
- **Summary:** Accepts a list of ingredients and returns usable items from the inventory.

**Request Body:**

    {
      "items": ["chicken", " ", "broccoli", "tomato", "  "]
    }


**Response**:

    {
      "usable_items": ["chicken", "broccoli", "tomato"],
      "message": "Filtered usable items successfully."
    }
---

### 3. Diet Endpoint
- **POST** /diet/
- **Summary**: Filters the available ingredients based on the specified diet.

**Request Body**:

    {
      "items": ["chicken", "tomato", "spinach"],
      "diet": "keto"
    }


**Response**:

    {
      "compatible_items": ["chicken", "spinach"],
      "suggested_recipe_ideas": ["Keto Chicken Stir Fry", "Spinach and Chicken Salad"]
    }

---

### 4. Planner Endpoint
- **POST** /plan/
- **Summary**: Accepts a base recipe and returns a step-by-step plan for preparation.

**Request Body**:

    {
      "base_recipe": "Chicken Stir Fry"
    }


**Response**:

    {
        "title": "Vegan Stir Fry Recipe",
        "ingredients": [
            "1 tablespoon vegetable oil",
            "1 onion, chopped",
            "2 cloves garlic, minced",
            "1 cup broccoli florets",
            "1 cup sliced bell peppers",
            "1 cup sliced carrots",
            "1 cup cooked tofu, cut into small pieces",
            "2 teaspoons soy sauce",
            "1 teaspoon grated ginger",
            "Salt and pepper to taste",
            "Chopped green onions for garnish"
        ],
        "steps": [
            {
                "step_number": 1,
                "instruction": "Heat the vegetable oil in a large skillet or wok over medium-high heat."
            },
            {
                "step_number": 2,
                "instruction": "Add the chopped onion and cook for 2-3 minutes, until it starts to soften."
            },
            {
                "step_number": 3,
                "instruction": "Add the minced garlic and cook for another minute, until fragrant."
            },
            {
                "step_number": 4,
                "instruction": "Add the broccoli, bell peppers, and carrots to the skillet. Cook for 5 minutes, until the vegetables start to tenderize."
            },
            {
                "step_number": 5,
                "instruction": "Add the cooked tofu, soy sauce, and grated ginger to the skillet. Stir to combine."
            },
            {
                "step_number": 6,
                "instruction": "Continue to cook for another 2-3 minutes, until the vegetables are tender and the sauce has thickened."
            },
            {
                "step_number": 7,
                "instruction": "Season with salt and pepper to taste, then garnish with chopped green onions."
            },
            {
                "step_number": 8,
                "instruction": "Serve the vegan stir fry hot over rice or noodles, and enjoy!"
            }
        ]
    }

---

### 5. Ask Endpoint
- **POST** /ask/
- **Summary**: Accepts a list of items and a diet type, and returns suggestions for meal planning.

**Request Body**:

    {
        "items":["tomato","chicken","spinach"],
        "diet":"keto"}
    }
    

**Response**:

    {
        "usable_items": [
            "tomato",
            "chicken",
            "spinach"
        ],
        "diet_filtered": [
            "chicken",
            "spinach",
            "tomato"
        ],
        "suggestions": [
            "Keto Chicken and Spinach Stir-Fry",
            "Baked Chicken and Tomato with Spinach",
            "Keto Chicken and Vegetable Kabobs with Spinach and Tomato"
        ]
    }

---

### 6. Recommend Endpoint
- **POST** /recommend/
- **Summary**: Recommends meal recipes based on available items and a specific diet.

**Request Body**:

    {
        "items":["tofu","bell pepper","garlic","oil"],
        "diet":"vegan",
        "recipe_count":2
    }


**Response**:

    {
    "recipes": [
        {
            "title": "Vegan Stir Fry",
            "ingredients": [
                "1 tablespoon of vegetable oil",
                "1 onion, sliced",
                "2 cloves of garlic, minced",
                "1 cup of broccoli florets",
                "1 cup of bell pepper slices",
                "1 cup of carrots, peeled and sliced",
                "1 cup of mushrooms, sliced",
                "2 teaspoons of soy sauce",
                "1 teaspoon of stir-fry sauce",
                "Salt and pepper to taste",
                "Chopped green onions for garnish"
            ],
            "steps": [
                {
                    "step_number": 1,
                    "instruction": "Heat the vegetable oil in a large skillet or wok over medium-high heat."
                },
                {
                    "step_number": 2,
                    "instruction": "Add the sliced onion to the skillet and cook for 2-3 minutes, or until it starts to soften."
                },
                {
                    "step_number": 3,
                    "instruction": "Add the minced garlic to the skillet and cook for another minute, stirring constantly to prevent burning."
                },
                {
                    "step_number": 4,
                    "instruction": "Add the broccoli, bell pepper, and carrots to the skillet, and cook for 4-5 minutes, or until they start to tenderize."
                },
                {
                    "step_number": 5,
                    "instruction": "Add the mushrooms to the skillet and cook for another 2-3 minutes, or until all the vegetables are tender-crisp."
                },
                {
                    "step_number": 6,
                    "instruction": "In a small bowl, whisk together the soy sauce and stir-fry sauce, and pour the mixture over the vegetables in the skillet."
                },
                {
                    "step_number": 7,
                    "instruction": "Stir everything together to combine, and cook for another minute to allow the flavors to meld."
                },
                {
                    "step_number": 8,
                    "instruction": "Season the stir-fry with salt and pepper to taste, and garnish with chopped green onions."
                },
                {
                    "step_number": 9,
                    "instruction": "Serve the vegan stir-fry hot over rice, noodles, or enjoy it on its own as a quick and easy meal."
                }
            ]
        },
        {
            "title": "Roasted Bell Pepper and Tofu Bowl",
            "ingredients": [
                "4 bell peppers, any color",
                "1 block of firm tofu, drained and cut into cubes",
                "2 tablespoons of olive oil",
                "1 onion, chopped",
                "2 cloves of garlic, minced",
                "1 teaspoon of cumin",
                "1 teaspoon of smoked paprika",
                "Salt and pepper, to taste",
                "4 cups of mixed greens",
                "1/4 cup of chopped fresh cilantro",
                "2 tablespoons of lemon juice",
                "1 avocado, sliced (optional)"
            ],
            "steps": [
                {
                    "step_number": 1,
                    "instruction": "Preheat the oven to 425°F (220°C). Place the bell peppers on a baking sheet, drizzle with 1 tablespoon of olive oil, and roast for 30-40 minutes, or until the skin is blistered and charred."
                },
                {
                    "step_number": 2,
                    "instruction": "While the bell peppers are roasting, heat the remaining 1 tablespoon of olive oil in a large skillet over medium-high heat. Add the chopped onion and cook for 3-4 minutes, or until softened."
                },
                {
                    "step_number": 3,
                    "instruction": "Add the minced garlic to the skillet and cook for 1 minute, or until fragrant."
                },
                {
                    "step_number": 4,
                    "instruction": "Add the cubed tofu to the skillet, sprinkle with cumin and smoked paprika, and cook for 5-7 minutes, or until the tofu is golden brown and crispy on all sides."
                },
                {
                    "step_number": 5,
                    "instruction": "Once the bell peppers are done roasting, remove them from the oven and let them cool down. Peel off the skin, remove the seeds, and slice them into strips."
                },
                {
                    "step_number": 6,
                    "instruction": "To assemble the bowls, divide the mixed greens among four bowls. Top with roasted bell pepper strips, cubed tofu, and a sprinkle of chopped cilantro."
                },
                {
                    "step_number": 7,
                    "instruction": "Drizzle the bowls with lemon juice and season with salt and pepper to taste. Top with sliced avocado, if desired."
                },
                {
                    "step_number": 8,
                    "instruction": "Serve immediately and enjoy!"
                }
            ]
        }
    ]
    }
---

This project was done as part of the fulfilment of the core topics of 'Introduction to AI Engineering with Python' HyperSkill course.
#### Learn more at:
https://hyperskill.org/projects/530

