import unittest
import os
from Persistence.DataManager import ConcreteDataManager
from Model.User import User
from app import app
from flask_sqlalchemy import SQLAlchemy
import tempfile

class TestDataManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setup that runs once before all tests
        cls.original_use_database = os.getenv('USE_DATABASE')
    
    @classmethod
    def tearDownClass(cls):
        if 'USE_DATABASE' in os.environ:
            del os.environ['USE_DATABASE']

    def setUp(self):
        # Setup that runs before each test
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_manager = ConcreteDataManager()
        if not self.data_manager.use_database:
            self.data_manager.storage_path = self.temp_dir.name  # Assuming DataManager can use a custom path

    def tearDown(self):
        if hasattr(self, 'temp_dir'):
            self.temp_dir.cleanup()
        super().tearDown()

    def test_create_user_db(self):
        with app.app_context():  # Push an application context
            user = User(email="testuser@example.com", first_name="Test", last_name="User", password="securepassword123")
            self.data_manager.save(user)
            # Assuming DataManager has a method to retrieve all users
            self.assertIn(user, self.data_manager.get_all(User))

    def test_create_user_file(self):
        os.environ['USE_DATABASE'] = 'False'
        self.data_manager.use_database = False
        user = User(email="testuser2@example.com", first_name="Test2", last_name="User2", password="securepassword123")
        self.data_manager.save(user)
        self.assertIn(user, self.data_manager.get_all(User))

# Additional tests for Read, Update, Delete, Relationships, and Dynamic Switching
    def setUp(self):
        super().setUp()
        # Insert test user
        user = User(email="testuser@example.com", first_name="Dupont", last_name="Dubois", password="password")
        self.data_manager = ConcreteDataManager()
        self.data_manager.save(user)

    def test_read_user_db(self):
        with app.app_context():  # Push an application context
            users = self.data_manager.get_all(User)
            self.assertIsNotNone(users)
            self.assertGreater(len(users), 0)

    def test_afficher_tous_les_utilisateurs(self):
        with app.app_context():
            # Étape 1 : Récupérer tous les utilisateurs
            tous_les_utilisateurs = self.data_manager.get_all(User)
        
        # Ouvrir un fichier en mode écriture
        with open('resultats_utilisateurs.txt', 'w') as fichier:
            # Étape 2 : Itérer et afficher les détails de chaque utilisateur dans le fichier
            for utilisateur in tous_les_utilisateurs:
                print(f"ID: {utilisateur.user_id}, Email: {utilisateur.email}, Prenom: {utilisateur.first_name} Nom: {utilisateur.last_name}", file=fichier)

            """def test_read_user(self):
        # Créer ou récupérer un utilisateur pour obtenir un identifiant valide
        user = User(email="testuser@example.com", first_name="Test2", last_name="User2", password="securepassword123")
        self.data_manager.save(user)  # Assurez-vous que cette méthode renvoie l'identifiant ou sauvegarde l'utilisateur de manière appropriée
        user_id = user.user_id  # Supposons que user_id est accessible et correct après la sauvegarde
    
        with app.app_context():
            user = self.data_manager.get(User, user_id)
            self.assertIsNotNone(user)
            self.assertEqual(user.user_id, user_id)  # Assurez-vous d'utiliser l'attribut correct pour l'identifiant
            self.assertEqual(user.email, "testuser@example.com")"""

if __name__ == '__main__':
    unittest.main()