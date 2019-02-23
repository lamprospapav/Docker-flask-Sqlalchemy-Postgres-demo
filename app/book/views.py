from flask import flash,redirect,render_template,url_for
from flask_login import login_required,current_user
from . import book
from .forms import BookForm
from .. import db
from ..models import Book,User


@book.route('/books', methods=['GET', 'POST'])
@login_required
def list_books():
    """
    List all objects
    """

    books = Book.query.filter_by(user_id = current_user.id).all()

    return render_template('book/books.html',
                           books=books, title="Books")

@book.route('/books/add',methods =['GET','POST'])
@login_required
def add_book():
    """
    Add an Object

    """
    form = BookForm()
    if form.validate_on_submit():
        book = Book(name = form.name.data,
                    rating = form.rating.data,
                    user_id = current_user.id)
        try:
            # add book to the database
            db.session.add(book)
            db.session.commit()
            flash('You have successfully added a new book.')
        except:
            # in case book name already exists
            flash('Error: book name already exists.')
        # redirect to departments page
        return redirect(url_for('book.list_books'))
    
    return render_template('book/book.html', action="Add",
                           add_book=add_book, form=form,
                           title="Add book")

@book.route('/books/edit/<int:id>',methods=['GET','POST'])
@login_required
def edit_book(id):
    """
    Edit book
   
    """
    book = Book.query.get_or_404(id)
    form = BookForm(obj = book)
    if form.validate_on_submit():
        book.name = form.name.data
        book.rating = form.rating.data
        db.session.commit()
        flash('You have successfully edited the book.')

        # redirect to the departments page
        return redirect(url_for('book.list_books'))

    form.rating.data = book.rating
    form.name.data = book.name
    return render_template('book/book.html', action="Edit",
                           add_book=add_book, form=form,
                           book=book, title="Edit book")

@book.route('/books/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_book(id):
    """
    Delete a book from the database
    """

    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash('You have successfully deleted the book.')

    # redirect to the departments page
    return redirect(url_for('book.list_books'))

    return render_template(title="Delete book")