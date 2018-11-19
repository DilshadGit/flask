from flask import (
    render_template,
    url_for,
    flash,
    redirect,
    request,
    abort,
    Blueprint,
)
from flask_login import (
    login_user,
    current_user,
    login_required,
)
from flaskpro import db
from flaskpro.models import Post, User
from flaskpro.posts.forms import (
    CreatePostForm,
    UpdatePostForm,
)


posts = Blueprint('posts', __name__)


@posts.route('/post/create', methods=['GET', 'POST'])
@login_required
def create_post():
    template_name = 'post_create.html'
    form = CreatePostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash(f'{post.title} has been successfully created.', 'success')
        return redirect(url_for('posts.post_list'))
    return render_template(template_name, title='Create new post', form=form, legend='Create New post')


@posts.route('/posts')
def post_list():
    template_name = 'posts.html'
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.created_date.desc()).paginate(page=page, per_page=3)
    return render_template(template_name, title='Post list', posts=posts)


@posts.route('/user/<string:username>')
def user_posts(username):
    template_name = 'user_posts.html'
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).order_by(
        Post.created_date.desc()).paginate(page=page, per_page=3)
    return render_template(template_name, title='User Post list', posts=posts, user=user)


@posts.route('/post/<int:post_id>')
def post_detail(post_id):
    template_name = 'post_detail.html'
    post = Post.query.get_or_404(post_id)
    return render_template(template_name, post=post, title=post.title)


@posts.route('/post/update/<int:post_id>', methods=['GET', 'POST'])
@login_required
def post_update(post_id):
    template_name = 'post_update.html'
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
        flash('Please be a ware that you only allowed to update own post!')
    form = UpdatePostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash(f'{current_user.username.upper()}, Your current post has been updated', 'success')
        return redirect(url_for('posts.post_detail', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template(template_name, title='Update Post', post=post, form=form, legend='Update Post')


@posts.route('/post/delete/<int:post_id>', methods=['POST'])
@login_required
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash(f'{current_user.username.upper()}, Your current post has ben deleted', 'success')
    return redirect(url_for('posts.post_list'))
