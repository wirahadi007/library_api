from app.models import Author, db

def get_all_authors():
    authors = Author.query.all()
    return [{'id': author.id, 'name': author.name} for author in authors]

def create_author(data):
    author = Author(name=data['name'], bio=data.get('bio'), birth_date=data.get('birth_date'))
    db.session.add(author)
    db.session.commit()
    return {'id': author.id, 'name': author.name}

def get_authors_byid(id):
    author =  Author.query.get_or_404(id)
    return {'id': author.id, 'name': author.name, 'bio': author.bio, 'birth_date': author.birth_date}

def update_author(id, data):
    author = Author.query.get_or_404(id)
    author.name = data['name']
    author.bio = data.get('bio')
    author.birth_date = data.get('birth_date')
    db.session.commit()
    return author

def delete_author(id):
    author = Author.query.get_or_404(id)
    db.session.delete(author)
    db.session.commit()

