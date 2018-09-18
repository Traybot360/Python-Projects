<!DOCTYPE html>
<html>
<!--  <img src="./avatar_img.png" alt="img" style="position: absolute;top:30px;left:50%;width:50px;"> -->
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <title>User Info</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.1/css/bulma.min.css">
    <script defer src="https://use.fontawesome.com/releases/v5.1.0/js/all.js"></script>
    <style>
        #div1 {
            width: 350px;
            height: 70px;
            padding: 10px;
            border: 1px solid #aaaaaa;
        }
    </style>
</head>
<script>
        function allowDrop(ev) {
            ev.preventDefault();
        }
        
        function drag(ev) {
            ev.dataTransfer.setData("text", ev.target.id);
        }
        
        function drop(ev) {
            ev.preventDefault();
            var data = ev.dataTransfer.getData("text");
            ev.target.appendChild(document.getElementById(data));
        }
</script>


<body style="text-align:center;">
        <div class="field">
                <label class="label">Logo (Drag and drop)</label>
                <div class="control">

                        <div id="div1" ondrop="drop(event)" ondragover="allowDrop(event)"></div>
                </div>
              </div>
              
              <div class="field">
                <label class="label">First Name And Last Name</label>
                <div class="control ">
                  <input class="input is-success" type="text" placeholder="First Name" required value="John ">
                  <input class="input is-success" type="text" placeholder="Last Name" required value=" Doe">


              </div>
              <div class="field">
                    <label class="label">Date of birth</label>
                    <div class="control ">
                      <input class="input is-primary" required type="text" placeholder="mm/dd/yyyy" value="">
 
                      
                    </div>
                  </div>
              
              <div class="field">
                <label class="label">Email</label>
                <div class="control ">
                  <input class="input is-primary"required type="email" placeholder="Email input" value="">

                  
                </div>
              </div>
              
              
              
              <div class="field">
                    <label class="label">Date Opened</label>
                    <div class="control ">
                      <p>1/1/1</p>
 
                      
                    </div>
                  </div>
              
              <div class="field">
                <div class="control">
                  <label class="checkbox">
                    <input type="checkbox">
                    I agree to the <a href="#">terms and conditions</a>
                  </label>
                </div>
              </div>
              
              <div class="field">
                <div class="control">
                    <label class="label">Gender</label>
                  <label class="radio">
                    <input type="radio" name="question">
                    Male
                  </label>
                  <label class="radio">
                    <input type="radio" name="question">
                    Female
                  </label>
                </div>
              </div>
              
              <div class="field is-grouped">
                <div class="control">
                  <button class="button is-link">Submit</button>
                </div>
                <div class="control">
                  <button class="button is-text">Cancel</button>
                </div>
              </div>
</body>

</html>
