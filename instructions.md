Pr lancer un enregistrement :
playwright codegen --target python --save-storage=auth.json https://xn--dmineur-bya.eu/

Pr lancer les autres fois, qd je serai déjà connecté :
playwright codegen --target python --load-storage=auth.json https://www.wiki-masters.com/login

playwright codegen --channel=chrome --user-data-dir=./profil https://www.wiki-masters.com/login
