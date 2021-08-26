<template>
    <div>
		<ul v-for="(post, index) in result" :key="index">
            <h1>
                <li>
                    {{ post.id }}
                </li>
            </h1>
            <h1>
                <li>
                    {{ post.content }}
                </li>
            </h1>
            <h1>
                <li>
                    {{ post.regist_date }}
                </li>
            </h1>
            <h1>
                <li>
                    {{ post.update_date }}
                </li>
            </h1>
		</ul>
	</div>
</template>

<script>
    export default {
        data() {
	        return {
	            result: null,
	        }
	    },
        async mounted(){
            const response = await this.$axios.get("hello/");
            this.result = response.data.results;
        },
	};
</script>