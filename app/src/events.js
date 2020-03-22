const express = require('express');
function createRouter(db) {
  const router = express.Router();
  // the routes are defined here
  router.post('/user', (req, res, next) => {
    db.query(
      'INSERT INTO user (uname, fname, lname, email, dob, password) VALUES (?,?,?,?,?,?)',
      [req.body.uname, req.body.fname, req.body.lname, req.body.email,new Date(req.body.dob), req.body.password],
      (error) => {
        if (error) {
          console.error(error);
          res.status(500).json({status: 'error'});
        } else {
          res.status(200).json({status: 'ok'});
        }
      }
    );
  });
  return router;
}
module.exports = createRouter;