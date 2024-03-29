from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    PermissionDenied,
    ValidationError,
)

from board.models import Post
from board.serializer import PostSerializer


class BoardViewSet(viewsets.ViewSet):
    """
    ### Board Viewset

    Literally.

    """

    def list(self, request):
        post_list = Post.objects.all()
        serializer = PostSerializer(post_list, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )

    def create(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )

        raise ValidationError(detail=serializer.errors)

    def retrieve(self, request, post_id):
        try:
            session = Post.objects.get(id=post_id)

            serializer = PostSerializer(session)

            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK,
            )

        except ObjectDoesNotExist:
            raise NotFound(
                detail="Object does not exist",
                code="not_found",
            )

    def update(self, request, post_id):
        try:
            sequence = Post.objects.get(id=post_id)

            if request.user == sequence.project.user:
                serializer = PostSerializer(
                    sequence,
                    data=request.data,
                    partial=True,
                )

                if serializer.is_valid():
                    serializer.save()

                    return Response(
                        data=serializer.data,
                        status=status.HTTP_200_OK,
                    )

                raise ValidationError(detail=serializer.errors)

            raise PermissionDenied(
                detail="You do not have permission to access this object",
                code="access_denied",
            )

        except ObjectDoesNotExist:
            raise NotFound(
                detail="Object does not exist",
                code="not_found",
            )

    def destroy(self, request, post_id):
        try:
            session = Post.objects.get(id=post_id)

            if request.user == session.user:
                session.delete()

                return Response(
                    status=status.HTTP_204_NO_CONTENT,
                )

            raise PermissionDenied(
                detail="You do not have permission to access this object",
                code="access_denied",
            )

        except ObjectDoesNotExist:
            raise NotFound(
                detail="Object does not exist",
                code="not_found",
            )
