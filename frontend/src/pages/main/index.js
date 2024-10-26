import { Card, Title, Pagination, CardList, Container, Main, CheckboxGroup  } from '../../components'
import styles from './styles.module.css'
import { useRecipes } from '../../utils/index.js'
import { useEffect } from 'react'
import api from '../../api'
import MetaTags from 'react-meta-tags'
import Board from '../../components/boardbox/board.js'

const HomePage = ({ updateOrders }) => {
  const {
    recipes,
    setRecipes,
    recipesCount,
    setRecipesCount,
    recipesPage,
    setRecipesPage,
    tagsValue,
    setTagsValue,
    handleTagsChange,
    handleLike,
    handleAddToCart
  } = useRecipes()


  const getRecipes = ({ page = 1, tag }) => {
    api
      .getRecipes({ page, tag })
      .then(res => {
        const { results, count } = res
        setRecipes(results)
        setRecipesCount(count)
      })
  }

  useEffect(_ => {
    getRecipes({ page: recipesPage, tags: tagsValue })
  }, [recipesPage, tagsValue])

  useEffect(_ => {
    api.getTags()
      .then(tags => {
        tags && setTagsValue(tags.map(tag => ({ ...tag, value: true })))
      })
  }, [])

  return <Main>
    <Container>
      <MetaTags>
        <title>Проекты</title>
        <meta name="description" content="Хакатон - Проекты" />
        <meta property="og:title" content="Проекты" />
      </MetaTags>
      <div className={styles.title}>
        <Title title='Проекты' />
      </div>
      <Board recipes={recipes}/>
      <Pagination
        count={recipesCount}
        limit={6}
        page={recipesPage}
        onPageChange={page => setRecipesPage(page)}
      />
    </Container>
  </Main>
}

export default HomePage

