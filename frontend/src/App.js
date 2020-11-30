import 'antd/dist/antd.css'; // or 'antd/dist/antd.less'
import { BrowserRouter, Route, Switch } from 'react-router-dom'

import { HomeLayout } from './Layouts/homeLayout';
import { LoginComponent } from './Components/Auth/loginComponents'
import { RegistrationForm } from './Components/Auth/signupComponent'
import { MenuComponent } from './Components/Navbar/navbarComponent'


//import { AuthLayout } from './Layouts/authLayout'

function App() {
  return (
    <BrowserRouter>
      <MenuComponent>
        
      </MenuComponent>
       <Switch>
          <Route exact path={"/login/"} component={LoginComponent}/>
          <Route exact path={"/signup/"} component={RegistrationForm}/>
          <Route exact path={"/"} component={HomeLayout}/>
        </Switch>
    </BrowserRouter>
  );
}

export default App;
