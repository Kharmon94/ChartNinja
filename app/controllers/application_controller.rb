class ApplicationController < ActionController::Base

    protected

    def after_sign_in_path_for(resource)
      user_profile_path(resource)
    end
  
    def after_sign_up_path_for(resource)
      user_profile_path(resource)
    end
  
end
