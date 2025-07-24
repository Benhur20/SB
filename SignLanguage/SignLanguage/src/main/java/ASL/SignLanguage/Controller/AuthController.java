package ASL.SignLanguage.Controller;

import ASL.SignLanguage.DTO.UserDTO;
import ASL.SignLanguage.Service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api") // All APIs will start with /api
@CrossOrigin(origins = "http://localhost:5173", allowCredentials = "true")
public class AuthController {

    @Autowired
    private UserService userService;

    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestParam String username,
                                   @RequestParam String password) {
        if (userService.login(username, password)) {
            return ResponseEntity.ok().body("Login successful");
        } else {
            return ResponseEntity.status(401).body("Invalid credentials");
        }
    }

    @PostMapping("/register")
    public ResponseEntity<?> register(@RequestBody UserDTO userDTO) {
        boolean success = userService.register(userDTO.getUserName(), userDTO.getPassword());
        if (success) {
            return ResponseEntity.ok().body("Registration successful");
        } else {
            return ResponseEntity.status(400).body("Username already exists");
        }
    }
}
