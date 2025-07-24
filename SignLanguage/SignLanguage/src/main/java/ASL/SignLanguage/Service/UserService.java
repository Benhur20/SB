package ASL.SignLanguage.Service;

import ASL.SignLanguage.DTO.ResponseDTO;
import ASL.SignLanguage.Repository.UserRepository;
import ASL.SignLanguage.Model.User; // <-- Use your entity class
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    private final UserRepository userRepo;

    public UserService(UserRepository userRepo) {
        this.userRepo = userRepo;
    }

    public boolean register(String username, String password) {
        if (userRepo.findByUserName(username) != null) return false;
        User user = new User();
        user.setUserName(username);
        user.setPassword(password);
        userRepo.save(user);
        return true;
    }

    public boolean login(String username, String password) {
        User user = userRepo.findByUserName(username);
        return user != null && user.getPassword().equals(password);
    }
}