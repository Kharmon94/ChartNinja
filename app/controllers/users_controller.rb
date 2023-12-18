class UsersController < ApplicationController
  before_action :authenticate_user!

  def show
    @user = User.find(params[:id])
    @charts = @user.charts
    # Ensure that the user can only access their own profile
    redirect_to(root_path) unless @user == current_user
  end
end
