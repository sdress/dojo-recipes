from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask import flash

@app.route('/recipes/<int:id>')
def show_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe_data = {
        'id': id
    }
    user_data = {
        'id': session['user_id']
    }
    return render_template('read_recipe.html', recipe=Recipe.get_from_id(recipe_data), user=User.get_from_id(user_data))

@app.route('/recipes/new')
def show_recipe_form():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('recipe_form.html')

@app.route('/create-recipe', methods = ['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'time': request.form['time'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'user_id': session['user_id']
        }
    Recipe.create(data)
    return redirect('/dashboard')

@app.route('/recipes/edit/<int:id>')
def show_edit_form(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': id
    }
    recipe=Recipe.get_from_id(data)
    print('recipe = ', recipe)
    return render_template('edit_form.html', recipe=recipe)

@app.route('/recipes/update/<int:id>', methods = ['POST'])
def update_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': id,
        'name': request.form['name'],
        'description': request.form['description'],
        'time': request.form['time'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'user_id': session['user_id']
        }
    Recipe.update(data)
    return redirect('/dashboard')

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': id
    }
    Recipe.delete(data)
    return redirect('/dashboard')