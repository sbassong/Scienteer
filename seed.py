# scienteer_id=
# researcher_id=
# s_token=
# r_token=
# #register - http://localhost:5000/auth/register
  #researcher user
  {
    "name":"researcher",
    "email": "r@email.com",
    "password": "test",
    "bio": "Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt amet quidem. Iusto deleniti cum autem ad quia aperiam.A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur quiquaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernaturvoluptatem sit aliquam. Dolores voluptatum est.Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.Et sint et. Ut ducimus quod nemo ab voluptatum.",
    "researcher": True
  }

  #scienteer user
  {
    "name":"scienteer",
    "email": "s@email.com",
    "password": "test",
    "bio": "Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt amet quidem. Iusto deleniti cum autem ad quia aperiam.A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur quiquaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernaturvoluptatem sit aliquam. Dolores voluptatum est.Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.Et sint et. Ut ducimus quod nemo ab voluptatum.",
    "researcher": False
  }

#login - http://localhost:5000/auth/login
{
  "email": "r@email.com",
  "password": "test"
}
{
  "email": "s@email.com",
  "password": "test"
}

#update userpass - http://localhost:5000/users/profile_pw/<string:id>
{
  "old_password": "test",
  "new_password": "testy",
}

#update userProfile - http://localhost:5000/users/profile/<string:id>
{
  "old_password": "test",
  "new_password": "testy",
}



#project_id=
#create project - http://localhost:5000/projects
{
  "title": "Orcas pod tracking",
  "user_id": ,
  "category": "ecology",
  "instructions": "Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt amet quidem. Iusto deleniti cum autem ad quia aperiam.A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur quiquaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernaturvoluptatem sit aliquam. Dolores voluptatum est.Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.Et sint et. Ut ducimus quod nemo ab voluptatum.",
  "requirements": "bio": "Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt amet quidem. Iusto deleniti cum autem ad quia aperiam.A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur quiquaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernaturvoluptatem sit aliquam. Dolores voluptatum est.Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.Et sint et. Ut ducimus quod nemo ab voluptatum.",
}

# projectbyid - http://localhost:5000/project/<int:id>
  #update body
  {
    "title": "Seals tracking",
    "user_id": ,
    "category": "ecology",
    "instructions": "Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt amet quidem. Iusto deleniti cum autem ad quia aperiam.A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur quiquaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernaturvoluptatem sit aliquam. Dolores voluptatum est.Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.Et sint et. Ut ducimus quod nemo ab voluptatum.",
    "requirements": "bio": "Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt amet quidem. Iusto deleniti cum autem ad quia aperiam.A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur quiquaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernaturvoluptatem sit aliquam. Dolores voluptatum est.Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.Et sint et. Ut ducimus quod nemo ab voluptatum.",
  }

# projectby user_id - http://localhost:5000/projects/researcher/<string:user_id>
# projectby user_id - http://localhost:5000/projects/category/<string:category>




#report_id=
#create report - http://localhost:5000/reports
{
  "content": "Orcas are doing well, much cute!",
  "user_id": ,
  "project_id": 
}

# reportbyid - http://localhost:5000/report/<string:id>
  #update body
  {
  "content": "Seals are doing well, great dogos!",
  "user_id": ,
  "project_id": 
  }


# report by project_id - http://localhost:5000/reports/project/<string:project_id>