# scienteer_id= 279084ba-8802-4f29-bb00-18d1a92d4d01
# researcher_id= c3cae0e1-5d3d-49c4-8875-942563a7f511

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



#project_id= e8845b0f-f4f9-401e-96a6-449e3d848d4b
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




# report_id=7ac4a80f-9870-4725-92a6-5a8a48680658
# create report - http://localhost:5000/reports OK
{
  "content": "Orcas are doing well, much cute!",
  "location": "point bob",
  "user_id": "279084ba-8802-4f29-bb00-18d1a92d4d01",
  "project_id": "e8845b0f-f4f9-401e-96a6-449e3d848d4b" 
}

# reportbyid - http://localhost:5000/report/7ac4a80f-9870-4725-92a6-5a8a48680658
  #update body
  {
  "content": "Seals are doing well, great dogos!",
  "location": "point bob",
  "user_id": "279084ba-8802-4f29-bb00-18d1a92d4d01",
  "project_id": "e8845b0f-f4f9-401e-96a6-449e3d848d4b" 
  }


# report by project_id - http://localhost:5000/reports/project/e8845b0f-f4f9-401e-96a6-449e3d848d4b   OK   <string:project_id>