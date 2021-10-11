# scienteer_id= 279084ba-8802-4f29-bb00-18d1a92d4d01
# researcher_id= c3cae0e1-5d3d-49c4-8875-942563a7f511
# s_token=
# r_token= eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6ImMzY2FlMGUxLTVkM2QtNDljNC04ODc1LTk0MjU2M2E3ZjUxMSIsImVtYWlsIjoickBlbWFpbC5jb20ifQ.XtQ9R5zgattngpGu5Ee-x3d07jtFPSMr0jiM2o6YTo8
# #register - http://localhost:5000/auth/register  OK
  #researcher user
  {
    "name":"researcher",
    "email": "r@email.com",
    "password": "test",
    "bio": "Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt amet quidem. Iusto deleniti cum autem ad quia aperiam.A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur quiquaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernaturvoluptatem sit aliquam. Dolores voluptatum est.Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.Et sint et. Ut ducimus quod nemo ab voluptatum.",
    "researcher": true
  }

  #scienteer user 
  {
    "name":"scienteer",
    "email": "s@email.com",
    "password": "test",
    "bio": "Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt amet quidem. Iusto deleniti cum autem ad quia aperiam.A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur quiquaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernaturvoluptatem sit aliquam. Dolores voluptatum est.Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.Et sint et. Ut ducimus quod nemo ab voluptatum.",
    "researcher": false
  }

#login - http://localhost:5000/auth/login OK
{
  "email": "r@email.com",
  "password": "test"
}
{
  "email": "s@email.com",
  "password": "test"
}

#update userpass - http://localhost:5000/users/profile_pw/<string:id> OK
{
  "old_password": "test",
  "new_password": "testy"
}

#update userProfile - http://localhost:5000/users/profile/<string:id> OK
{
    "name":"researcher2",
    "email": "r@email.com",
    "password": "test",
    "bio": "Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt amet quidem. Iusto deleniti cum autem ad quia aperiam.A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur quiquaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernaturvoluptatem sit aliquam. Dolores voluptatum est.Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.Et sint et. Ut ducimus quod nemo ab voluptatum.",
    "researcher": true
}



#project_id= 1a8fabf5-d520-4156-bc3d-9ea7887c8eec
#create project - http://localhost:5000/projects OK
{
  "title": "Orcas pod tracking",
  "user_id": "c3cae0e1-5d3d-49c4-8875-942563a7f511",
  "category": "ecology",
  "instructions": "Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt amet quidem. Iusto deleniti cum autem ad quia aperiam.A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur quiquaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernaturvoluptatem sit aliquam. Dolores voluptatum est.Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.Et sint et. Ut ducimus quod nemo ab voluptatum.",
  "requirements": "Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt amet quidem. Iusto deleniti cum autem ad quia aperiam.A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur quiquaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernaturvoluptatem sit aliquam. Dolores voluptatum est.Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.Et sint et. Ut ducimus quod nemo ab voluptatum."
}

# projectbyid - http://localhost:5000/project/1a8fabf5-d520-4156-bc3d-9ea7887c8eec OK     <string:id>
  #update body
  {
    "title": "Seals tracking",
    "user_id": "c3cae0e1-5d3d-49c4-8875-942563a7f511",
    "category": "ecology",
    "instructions": "Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt amet quidem. Iusto deleniti cum autem ad quia aperiam.A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur quiquaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernaturvoluptatem sit aliquam. Dolores voluptatum est.Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.Et sint et. Ut ducimus quod nemo ab voluptatum.",
    "requirements": "Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt amet quidem. Iusto deleniti cum autem ad quia aperiam.A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur quiquaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernaturvoluptatem sit aliquam. Dolores voluptatum est.Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.Et sint et. Ut ducimus quod nemo ab voluptatum."
}

# projectby user_id - http://localhost:5000/projects/researcher/c3cae0e1-5d3d-49c4-8875-942563a7f511 OK      <string:user_id>
# projectby category - http://localhost:5000/projects/category/ecology OK        <string:category>




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