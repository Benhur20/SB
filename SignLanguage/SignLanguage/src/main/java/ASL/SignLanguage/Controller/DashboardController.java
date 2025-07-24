package ASL.SignLanguage.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class DashboardController {

    @GetMapping({"/", "/dashboard", "/register"})
    public String index() {
        return "forward:/index.html"; // ✅ Always serve React's index.html
    }
}
