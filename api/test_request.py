{
	questionList(id:1){
    title    
  },
  answerList(id:1){
    answerText
  }
  
}

# OR 
query GetQuestion($id: Int = 1) {
  questionList(id: $id) {
    title
  }
  answerList(id: 1) {
    answerText
  }
}


# Response:
{
  "data": {
    "questionList": {
      "title": "Who discovered the Lactometer?"
    },
    "answerList": [
      {
        "answerText": "Mr. Dicas"
      },
      {
        "answerText": "Mr. Bikas"
      },
      {
        "answerText": "Mr. Thomas"
      },
      {
        "answerText": "Dr. Jofra"
      }
    ]
  }
}

# 2. Add new category:
mutation addMutation {
  addCategory(name: "Computer") {
    category{
      name
    }
  }
}

# Response
{
  "data": {
    "addCategory": {
      "category": {
        "name": "Computer"
      }
    }
  }
}
# 3. Update Category 
mutation updateMutation {
  updateCategory(name: "Health and disease and data", id: 6) {
    category{
      name
      id
    }
  }
}

# Response:
{
  "data": {
    "updateCategory": {
      "category": {
        "name": "Health and disease",
        "id": "6"
      }
    }
  }
}

