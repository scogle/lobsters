class SignupController < ApplicationController

  def index
    if @user
      flash[:error] = "You are already signed up."
      return redirect_to "/"
    end
    @title = "Signup"
    @new_user = User.new
  end

  def signup

    @title = "Signup"
    @new_user = User.new(user_params)

    if @new_user.save
      session[:u] = @new_user.session_token
      flash[:success] = "Welcome to #{Rails.application.name}, " <<
        "#{@new_user.username}!"

      Countinual.count!("#{Rails.application.shortname}.users.created", "+1")

      #
    end
    return redirect_to "/"
  end

private

  def user_params
    params.require(:user).permit(
      :username, :email, :password, :password_confirmation, :about,
    )
  end
end
