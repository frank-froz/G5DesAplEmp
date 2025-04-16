from django.contrib import admin
from .recommendations import get_recommendations

def create_recommendation_admin_action():
    """Create an admin action for movie recommendations"""
    
    @admin.action(description="Get movie recommendations")
    def get_user_recommendations(modeladmin, request, queryset):
        """Action to get recommendations for selected users"""
        for profile in queryset:
            user = profile.user
            recommendations = get_recommendations(user, limit=5)
            recommendation_list = ", ".join([movie.title for movie in recommendations])
            modeladmin.message_user(
                request, 
                f"Recommendations for {user.username}: {recommendation_list}"
            )
    
    return get_user_recommendations
