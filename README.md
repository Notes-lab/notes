# Encrypted Notes

A note-taking app with option to encrypt text.
<br>
<br>
## Key Features
<br>
<ul>
  <li>At first you need to register then you should log in to your account</li>
  <li>Every note has category - you can create category</li>
  <li>Notes - you can create edit, and delete a note. When you want to create a note, you also need to create a password </li>
  <li>Note is password protected - you need to enter password to see text of note and edit it</li>
</ul>
<br>
<br>
<h2>How To Use</h2>
<br>
<div class="container">
  <p>Clone this repository:<br>
    <code>$ git clone https://github.com/Notes-lab/notes.git</code>
  </p>
  <p>Go into notes:<br>
    <code>$ cd notes</code>
  </p>
  <p>Activate a new virtual environment with pipenv shell:<br>
    <code>$ pipenv shell</code>
  </p>
  <p>Install dependencies:<br>
    <code>$ pipenv install --dev</code>
  </p>
  <p>Execute the migrate command to create an initial database :<br>
    <code>$ python manage.py migrate</code>
  </p>
  <p>Run local web server this project:<br>
    <code>$ python manage.py runserver 8000</code>
  </p>
</div>
