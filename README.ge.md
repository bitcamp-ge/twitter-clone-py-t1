# Twitter Clone

[English][en] - **[ქართული][ge]**

Twitter-ის კლონის პროექტი.

# კოდის გაშვება

1. შექმენით პროექტის ლოკალური ასლი: `git clone https://github.com/bitcamp-ge/twitter-clone-py-t1`
0. შეცვალეთ დირექტორია პროექტის დირექტორიაში: `cd twitter-clone-py-t1`
0. შექმენით Python-ის ვირტუალური გარემო: `python -m venv venv`
0. გააქტიურეთ Python-ის ვირტუალური გარემო
0. დააინსტალირეთ Python-ის დამოკიდებულებები: `pip install -r requirements.txt`
0. შექმენით Django-ს მიგრაციები: `python manage.py makemigrations`
0. გაუშვით Django-ს მიგრაციები: `python manage.py migrate`
0. ჩატვირთეთ საწყისი მონაცემთა ბაზა: `python manage.py loaddata initial_data.json`
0. გაუშვით Django-ს სერვერი: `python manage.py runserver localhost:8000`

> #### Note
> - Superuser-ის სახელი: `root`
> - Superuser-ის პაროლი: `root`

# როგორ გააქტიურო Python-ის ვირტუალური გარემო

### Linux/Unix-ის მომხმარებლებისთვის
- bash/zsh - `source ./venv/bin/activate`
- fish - `source ./venv/bin/activate.fish`
- csh/tcsh - `source ./venv/bin/activate.csh`

### Windows-ის მომხმარებლებისთვის
- PowerShell
- - კოდის გაშვების ნება დართეთ - `Set-ExecutionPolicy RemoteSigned`
- - გაუშვით აქტივაციის კოდი - `.\venv\Scripts\Activate.ps1`
- cmd.exe - `.\venv\Scripts\activate.bat`

[en]: https://github.com/bitcamp-ge/twitter-clone-py-t1#readme
[ge]: README.ge.md