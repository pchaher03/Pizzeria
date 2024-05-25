package com.example.pizzeria.User;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import com.example.pizzeria.User.User;
import com.example.pizzeria.User.UserService;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.RequestBody;


@RestController
@RequestMapping(path = "users")
public class UserController {
    private final UserService userService;

    @Autowired
    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("/getUsers")
    public List<User> getUsers() {
        return this.userService.getUsers();
    }

    @PostMapping("/registerUser")
    public ResponseEntity<Object> registerUser(@RequestBody User user) {        
        return this.userService.registerUser(user);
    }

    @PutMapping("/updateUser")
    public ResponseEntity<Object> updateUser(@RequestBody User user) {        
        return this.userService.updateUser(user);
    }

    @DeleteMapping("/deleteUser/{userId}")
    public ResponseEntity<Object> deleteUser(@PathVariable("userId") Long id) {        
        return this.userService.deleteUser(id);
    }


    
}
